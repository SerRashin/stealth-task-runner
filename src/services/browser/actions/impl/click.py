import re, time
from selenium.webdriver.support.ui import WebDriverWait
from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
class ClickAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "click"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action; tmo = int(act.get("timeout", job.context.timeout_sec*1000))
        el = wait_for(driver, act["by"], act["value"], "visible", tmo)
        expect = act.get("expect_popup")
        if expect:
            before = set(driver.window_handles); el.click()
            tt = int(expect.get("timeout", tmo))
            WebDriverWait(driver, tt/1000.0).until(lambda d: len(set(d.window_handles)-before)==1)
            new_h = list(set(driver.window_handles)-before)[0]
            alias2 = expect.get("alias", f"popup_{int(time.time()*1000)}")
            wins.set(alias2, new_h); driver.switch_to.window(new_h)
            if expect.get("url_regex"):
                WebDriverWait(driver, tt/1000.0).until(lambda d: re.search(expect["url_regex"], d.current_url or "") is not None)
        else:
            el.click()
handler = ClickAction()
