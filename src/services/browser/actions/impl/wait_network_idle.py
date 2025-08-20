import time
from selenium.webdriver.support.ui import WebDriverWait
from src.services.browser.actions.base import ActionInterface
class WaitNetworkIdleAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "wait_network_idle"
    def execute(self, driver, wins, step, job, res) -> None:
        tmo = int(step.action.get("timeout", job.context.timeout_sec*1000))
        WebDriverWait(driver, tmo/1000.0).until(lambda d: d.execute_script("return document.readyState") == "complete")
        time.sleep(float(step.action.get("extra_sleep_sec", 0.8)))
handler = WaitNetworkIdleAction()
