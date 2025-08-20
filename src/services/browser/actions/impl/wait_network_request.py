from selenium.webdriver.support.ui import WebDriverWait
from src.services.browser.actions.base import ActionInterface
class WaitNetworkRequestAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "wait_network_request"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action
        tmo = int(act.get("timeout", job.context.timeout_sec*1000))
        url_sub = act.get("url")
        WebDriverWait(driver, tmo/1000.0).until(lambda d: d.execute_script("return (window.__netlog && window.__netlog.reqs) ? window.__netlog.reqs : []"))
        def cond(d):
            try:
                logs = d.execute_script("return window.__netlog ? window.__netlog.reqs : []") or []
                return any(url_sub in (r.get("url") or "") for r in logs)
            except Exception:
                return False
        WebDriverWait(driver, tmo/1000.0).until(cond)
handler = WaitNetworkRequestAction()
