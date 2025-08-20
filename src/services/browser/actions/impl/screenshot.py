import base64, time
from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
class ScreenshotAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "screenshot"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action
        name = act.get("name", f"shot_{int(time.time())}")
        if act.get("full_page"): png = driver.get_screenshot_as_png()
        elif "by" in act:
            el = wait_for(driver, act["by"], act["value"], "visible", job.context.timeout_sec*1000); png = el.screenshot_as_png
        else: png = driver.get_screenshot_as_png()
        res.setdefault("screenshots", {})[name] = base64.b64encode(png).decode()
handler = ScreenshotAction()
