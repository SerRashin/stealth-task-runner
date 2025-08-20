from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
class InputTextAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "input_text"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action
        tmo = int(act.get("timeout", job.context.timeout_sec*100*10))
        el = wait_for(driver, act["by"], act["value"], "visible", tmo)
        if act.get("clear", True): el.clear()
        txt, delay = act.get("text",""), int(act.get("delay_ms",0))
        import time
        if delay>0:
            for ch in txt: el.send_keys(ch); time.sleep(delay/1000.0)
        else:
            el.send_keys(txt)
handler = InputTextAction()
