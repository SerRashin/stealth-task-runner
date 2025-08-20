from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.common.exceptions import WebDriverException

def by_from_str(by: str):
    return {
        "css": By.CSS_SELECTOR,
        "xpath": By.XPATH,
        "id": By.ID,
        "name": By.NAME,
        "class": By.CLASS_NAME,
        "tag": By.TAG_NAME,
        "link_text": By.LINK_TEXT,
        "partial_link_text": By.PARTIAL_LINK_TEXT
    }[by]

def wait_for(driver: Chrome, by: str, value: str, state: str, timeout_ms: int):
    b = by_from_str(by)
    w = WebDriverWait(driver, timeout_ms/1000.0)
    if state == "visible":   return w.until(EC.visibility_of_element_located((b, value)))
    if state in ("present","attached"): return w.until(EC.presence_of_element_located((b, value)))
    if state in ("hidden","invisible","detached"): return w.until(EC.invisibility_of_element_located((b, value)))
    return w.until(EC.presence_of_element_located((b, value)))

def find_all(driver: Chrome, by: str, value: str):
    return driver.find_elements(by_from_str(by), value)

def get_text(driver: Chrome, el, attr: str):
    if attr in ("innerText","textContent","text"):
        try:
            return driver.execute_script("return arguments[0].innerText", el) if attr != "text" else el.text
        except WebDriverException:
            return el.text
    return el.get_attribute(attr)
