import base64, time
from src.services.browser.actions.base import ActionInterface
class SavePdfAction(ActionInterface):
    def supports(self, type_str: str) -> bool: return type_str == "save_pdf"
    def execute(self, driver, wins, step, job, res) -> None:
        pdf = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})
        res.setdefault("files", {})[step.action.get("name", f"page_{int(time.time())}.pdf")] = pdf.get("data")
handler = SavePdfAction()
