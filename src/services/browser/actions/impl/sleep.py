import time
from src.services.browser.actions.base import ActionInterface
class SleepAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "sleep"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action; time.sleep(float(act.get("sec", act.get("ms", 500)/1000.0)))
handler = SleepAction()
