from src.services.browser.actions.base import ActionInterface
class ReloadAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "reload"
    def execute(self, driver, wins, step, job, res) -> None: driver.refresh()
handler = ReloadAction()
