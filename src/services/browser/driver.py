import os
import undetected_chromedriver as uc
from selenium.webdriver import Chrome
from src.core.config import UC_DOWNLOAD_DIR

def build_driver(ctx) -> Chrome:
    os.makedirs(UC_DOWNLOAD_DIR, exist_ok=True)
    opts = uc.ChromeOptions()
    prefs = {
        "download.default_directory": UC_DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    opts.add_experimental_option("prefs", prefs)
    if ctx.headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument(f"--window-size={ctx.viewport['width']},{ctx.viewport['height']}")
    opts.add_argument(f"--lang={ctx.locale}")
    if ctx.user_agent:
        opts.add_argument(f"--user-agent={ctx.user_agent}")
    if ctx.proxy:
        opts.add_argument(f"--proxy-server={ctx.proxy}")
    driver = uc.Chrome(options=opts, use_subprocess=True)
    driver.set_page_load_timeout(ctx.timeout_sec)
    return driver
