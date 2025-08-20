from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for, find_all, get_text
class ExtractAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "extract"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action; tmo = int(act.get("timeout", job.context.timeout_sec*1000))
        out = {}
        for it in act["items"]:
            by, value = it["by"], it["value"]
            attr = it.get("attr","innerText"); many = bool(it.get("all", False))
            if many:
                out[it["name"]] = [get_text(driver, e, attr) for e in find_all(driver, by, value)]
            else:
                try:
                    el = wait_for(driver, by, value, "visible", tmo)
                    out[it["name"]] = get_text(driver, el, attr)
                except Exception:
                    out[it["name"]] = None
        res["data"].update(out)
handler = ExtractAction()
