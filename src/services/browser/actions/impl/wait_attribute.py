import re
from selenium.webdriver.support.ui import WebDriverWait
from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import by_from_str
class WaitAttributeAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "wait_attribute"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action; tmo = int(act.get("timeout", job.context.timeout_sec*1000))
        sel = (by_from_str(act["by"]), act["value"]); name = act["name"]; val = act.get("equals"); rx = act.get("regex")
        def cond(d):
            try:
                el = d.find_element(*sel); a = el.get_attribute(name)
                if val is not None: return a == str(val)
                if rx: return re.search(rx, a or "") is not None
                return a is not None
            except Exception: return False
        WebDriverWait(driver, tmo/1000.0).until(cond)
handler = WaitAttributeAction()
