from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
class RemoveAttributeAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "remove_attribute"
    def execute(self, driver, wins, step, job, res) -> None:
        el = wait_for(driver, step.action["by"], step.action["value"], "present", job.context.timeout_sec*1000)
        driver.execute_script("arguments[0].removeAttribute(arguments[1]);", el, step.action["attr"])
handler = RemoveAttributeAction()
