from src.services.browser.actions.base import ActionInterface
class ScrollAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "scroll"
    def execute(self, driver, wins, step, job, res) -> None:
        act = step.action; to, x, y = act.get("to"), int(act.get("x",0)), int(act.get("y",0))
        if to == "bottom": driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        elif to == "top": driver.execute_script("window.scrollTo(0, 0);")
        else: driver.execute_script(f"window.scrollBy({x},{y});")
handler = ScrollAction()
