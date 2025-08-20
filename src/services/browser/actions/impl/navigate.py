from src.services.browser.actions.base import ActionInterface
class NavigateAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "navigate"
    def execute(self, driver, wins, step, job, res) -> None:
        driver.get(step.action["url"])
handler = NavigateAction()
