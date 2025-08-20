from src.services.browser.actions.base import ActionInterface
class BackAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "back"
    def execute(self, driver, wins, step, job, res) -> None: driver.back()
handler = BackAction()
