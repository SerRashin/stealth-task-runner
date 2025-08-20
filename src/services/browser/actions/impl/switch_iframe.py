from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
class SwitchIframeAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "switch_iframe"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action
        if "by" in act: el = wait_for(driver, act["by"], act["value"], "present", job.context.timeout_sec*1000); driver.switch_to.frame(el)
        elif "index" in act: driver.switch_to.frame(int(act["index"]))
handler = SwitchIframeAction()
