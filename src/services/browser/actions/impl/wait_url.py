import re
from selenium.webdriver.support.ui import WebDriverWait
from src.services.browser.actions.base import ActionInterface
class WaitUrlAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "wait_url"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action; tmo = int(act.get("timeout", job.context.timeout_sec*1000))
        rx, eq = act.get("regex"), act.get("equals")
        if rx: WebDriverWait(driver, tmo/1000.0).until(lambda d: re.search(rx, d.current_url or "") is not None)
        else: WebDriverWait(driver, tmo/1000.0).until(lambda d: (d.current_url or "") == eq)
handler = WaitUrlAction()
