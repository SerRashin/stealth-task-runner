from src.services.browser.actions.base import ActionInterface
class EvalJsAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "eval_js"
    def execute(self, driver, wins, step, job, res) -> None:
        val = driver.execute_script(step.action["script"]); res.setdefault("logs", []).append({"eval_js": val})
handler = EvalJsAction()
