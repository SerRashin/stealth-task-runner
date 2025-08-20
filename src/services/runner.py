from fastapi import HTTPException
from selenium.webdriver import Chrome
from src.models.job import Job
from src.models.action import Action
from src.services.browser.driver import build_driver
from src.services.browser.windows import Windows, switch_to
from src.services.netlog.inject import NETLOG_JS
from src.utils.render import render_vars
from src.services.browser.actions import get_registry, load_all_handlers

class Flow:
    def __init__(self):
        self.stack = []
        self.skip = False
    def push_if(self, cond: bool): self.stack.append(cond); self._recalc()
    def else_(self):
        if not self.stack: raise HTTPException(400, "else without if")
        self.stack[-1] = not self.stack[-1]; self._recalc()
    def pop_if(self):
        if not self.stack: raise HTTPException(400, "endif without if")
        self.stack.pop(); self._recalc()
    def _recalc(self): self.skip = not all(self.stack) if self.stack else False

class Runner:
    def __init__(self):
        load_all_handlers()
        self.registry = get_registry()

    def run(self, job: Job):
        driver: Chrome = None
        try:
            job = Job(**render_vars(job.dict(), job.vars))

            driver = build_driver(job.context)
            wins = Windows(map={})
            driver.get("about:blank")
            wins.set("main", driver.current_window_handle)

            if job.context.cookies:
                driver.get(job.url)
                for c in job.context.cookies:
                    cc = {k: c[k] for k in ("name","value") if k in c}
                    for k in ("domain","path","expiry","httpOnly","secure","sameSite"):
                        if k in c: cc[k] = c[k]
                    driver.add_cookie(cc)

            driver.get(job.url)
            try: driver.execute_script(NETLOG_JS)
            except Exception: pass

            result = {"ok": True, "final_url": None, "html": None,
                      "data": {}, "screenshots": {}, "downloads": [], "logs": [], "vars": {}}
            flow = Flow()

            for step in job.actions:
                when = step.action.get("when")
                if when and isinstance(when, dict) and "js" in when:
                    if not bool(driver.execute_script(when["js"])): continue

                if step.type == "if":
                    flow.push_if(bool(driver.execute_script(step.action["js"]))); continue
                if step.type == "else":
                    flow.else_(); continue
                if step.type == "endif":
                    flow.pop_if(); continue
                if step.type == "loop_while":
                    max_iter = int(step.action.get("max_iter", 10)); i = 0
                    while bool(driver.execute_script(step.action["js"])) and i < max_iter:
                        for sub in step.action.get("body", []):
                            self._dispatch(driver, wins, Action(**sub), job, result)
                        i += 1
                    continue

                if flow.skip: continue
                self._dispatch(driver, wins, step, job, result)

            if job.return_.get("html"):
                result["html"] = driver.page_source
            result["final_url"] = driver.current_url
            return result

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(500, detail=str(e))
        finally:
            try:
                if driver: driver.quit()
            except Exception:
                pass

    def _dispatch(self, driver, wins, step, job, res):
        switch_to(driver, wins, step.target)
        handler = self.registry.find(step.type)
        if not handler:
            raise HTTPException(400, f"No handler for action type: {step.type}")
        handler.execute(driver, wins, step, job, res)
