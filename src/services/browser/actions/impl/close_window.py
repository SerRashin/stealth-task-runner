from src.services.browser.actions.base import ActionInterface
class CloseWindowAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "close_window"
    def execute(self, driver, wins, step, job, res) -> None: driver.close()
handler = CloseWindowAction()
