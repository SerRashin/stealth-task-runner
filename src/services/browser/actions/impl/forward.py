from src.services.browser.actions.base import ActionInterface
class ForwardAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "forward"
    def execute(self, driver, wins, step, job, res) -> None: driver.forward()
handler = ForwardAction()
