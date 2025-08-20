from src.services.browser.actions.base import ActionInterface
from src.services.browser.waits import wait_for
class UploadFileAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "upload_file"
    def execute(self, driver, wins, step, job, res) -> None:
        el = wait_for(driver, step.action["by"], step.action["value"], "visible", job.context.timeout_sec*1000)
        el.send_keys(step.action["path"])
handler = UploadFileAction()
