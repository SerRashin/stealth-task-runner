from src.services.browser.actions.base import ActionInterface
class SwitchParentFrameAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "switch_parent_frame"
    def execute(self, driver, wins, step, job, res) -> None: driver.switch_to.parent_frame()
handler = SwitchParentFrameAction()
