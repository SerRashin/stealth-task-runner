from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
class ScrollIntoViewAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "scroll_into_view"
    def execute(self, driver, wins, step, job, res) -> None:
        el = wait_for(driver, step.action["by"], step.action["value"], "present", job.context.timeout_sec*1000)
        driver.execute_script("arguments[0].scrollIntoView({block:'center',inline:'center'});", el)
handler = ScrollIntoViewAction()
