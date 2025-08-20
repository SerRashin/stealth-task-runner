from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
class WaitAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "wait"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action
        tmo = int(act.get("timeout", job.context.timeout_sec*1000))
        wait_for(driver, act["by"], act["value"], act.get("state","visible"), tmo)
handler = WaitAction()
