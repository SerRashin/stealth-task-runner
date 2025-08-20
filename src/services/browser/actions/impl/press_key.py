from src.services.browser.actions.base import ActionInterface
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class PressKeyAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "press_key"
    def execute(self, driver, wins, step, job, res) -> None:
        keys = step.action["keys"]
        chain = ActionChains(driver)
        if len(keys) > 1:
            chain.key_down(getattr(Keys, keys[0].upper(), keys[0]))
            for k in keys[1:]: chain.send_keys(getattr(Keys, k.upper(), k))
            chain.key_up(getattr(Keys, keys[0].upper(), keys[0])).perform()
        else:
            chain.send_keys(getattr(Keys, keys[0].upper(), keys[0])).perform()
handler = PressKeyAction()
