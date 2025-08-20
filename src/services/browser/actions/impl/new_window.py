from src.services.browser.actions.base import ActionInterface
class NewWindowAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "new_window"
    def execute(self, driver, wins, step, job, res) -> None:
        url = step.action.get("url","about:blank"); before = set(driver.window_handles)
        driver.execute_script("window.open(arguments[0], '_blank');", url)
        after = set(driver.window_handles); new_h = list(after - before)[0]
        wins.set(step.action.get("alias","win_new"), new_h); driver.switch_to.window(new_h)
handler = NewWindowAction()
