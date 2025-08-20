from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
from selenium.webdriver.common.action_chains import ActionChains
class RightClickAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "right_click"
    def execute(self, driver, wins, step, job, res) -> None:
        el = wait_for(driver, step.action["by"], step.action["value"], "visible", job.context.timeout_sec*1000)
        ActionChains(driver).context_click(el).perform()
handler = RightClickAction()
