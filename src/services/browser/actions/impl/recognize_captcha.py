from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
from src.services.captcha.factory import get_captcha_service

class RecognizeCaptchaAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "recognize_captcha"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action
        tmo = int(act.get("timeout", job.context.timeout_sec*1000))
        el = wait_for(driver, act["by"], act["value"], "visible", tmo)
        img = el.screenshot_as_png
        provider = act.get("provider")  # provider is specified in the action now
        svc = get_captcha_service(provider)
        text = svc.solve(img)
        res["logs"].append({"captcha_provider": provider or "env_default", "captcha_text": text})
        target = act.get("recognize")
        if isinstance(target, str) and target.startswith("$"):
            res["vars"][target.lstrip("$")] = text
handler = RecognizeCaptchaAction()
