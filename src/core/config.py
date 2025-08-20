import os

UC_DOWNLOAD_DIR = os.getenv("UC_DOWNLOAD_DIR", "/tmp/uc_downloads")
DEFAULT_CAPTCHA_PROVIDER = os.getenv("DEFAULT_CAPTCHA_PROVIDER", "twocaptcha")
CAPTCHA_API_KEY = os.getenv("CAPTCHA_API_KEY", "")
CAPTCHA_POLL_SEC = float(os.getenv("CAPTCHA_POLL_SEC", "5"))
CAPTCHA_MAX_TRIES = int(os.getenv("CAPTCHA_MAX_TRIES", "20"))
