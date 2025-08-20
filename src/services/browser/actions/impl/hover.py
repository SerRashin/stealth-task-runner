from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
from selenium.webdriver.common.action_chains import ActionChains
class HoverAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "hover"
    def execute(self, driver, wins, step, job, res) -> None:
        el = wait_for(driver, step.action["by"], step.action["value"], "visible", job.context.timeout_sec*1000)
        ActionChains(driver).move_to_element(el).perform()
handler = HoverAction()
