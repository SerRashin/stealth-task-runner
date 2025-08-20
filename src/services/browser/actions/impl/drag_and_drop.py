from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
from selenium.webdriver.common.action_chains import ActionChains
class DragAndDropAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "drag_and_drop"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action
        src = wait_for(driver, act["source_by"], act["source_value"], "visible", job.context.timeout_sec*1000)
        dst = wait_for(driver, act["target_by"], act["target_value"], "visible", job.context.timeout_sec*1000)
        ActionChains(driver).drag_and_drop(src, dst).perform()
handler = DragAndDropAction()
