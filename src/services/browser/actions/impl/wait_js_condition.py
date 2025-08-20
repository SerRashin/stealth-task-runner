from selenium.webdriver.support.ui import WebDriverWait
from src.services.browser.actions.base import ActionInterface
class WaitJsConditionAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "wait_js_condition"
    def execute(self, driver, wins, step, job, res) -> None:
        tmo = int(step.action.get("timeout", job.context.timeout_sec*1000))
        WebDriverWait(driver, tmo/1000.0).until(lambda d: bool(d.execute_script(step.action["script"])))
handler = WaitJsConditionAction()
