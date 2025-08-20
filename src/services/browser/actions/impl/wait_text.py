import re
from selenium.webdriver.support.ui import WebDriverWait
from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for, get_text
class WaitTextAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "wait_text"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action; tmo = int(act.get("timeout", job.context.timeout_sec*1000))
        el = wait_for(driver, act["by"], act["value"], "visible", tmo)
        eq, rx = act.get("equals"), act.get("regex")
        if eq is not None: WebDriverWait(driver, tmo/1000.0).until(lambda d: get_text(d, el, "innerText") == eq)
        else: WebDriverWait(driver, tmo/1000.0).until(lambda d: re.search(rx, get_text(d, el, "innerText") or "") is not None)
handler = WaitTextAction()
