from selenium.webdriver.support.ui import Select
from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
class SelectOptionAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "select_option"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action; tmo = int(act.get("timeout", job.context.timeout_sec*1000))
        el = wait_for(driver, act["by"], act["value"], "visible", tmo)
        ch = act["choose"]; sel = Select(el)
        if "label" in ch: sel.select_by_visible_text(ch["label"])
        elif "value" in ch: sel.select_by_value(ch["value"])
        elif "index" in ch: sel.select_by_index(int(ch["index"]))
        else: raise Exception("select_option.choose must contain label|value|index")
handler = SelectOptionAction()
