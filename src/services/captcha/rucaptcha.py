import time, requests
from src.core.config import CAPTCHA_API_KEY, CAPTCHA_MAX_TRIES, CAPTCHA_POLL_SEC
from src.services.captcha.base import CaptchaInterface

class RuCaptchaService(CaptchaInterface):
    def solve(self, image_bytes: bytes) -> str:
        if not CAPTCHA_API_KEY:
            return "[NO_API_KEY]"
        try:
            r = requests.post(
                "http://rucaptcha.com/in.php",
                data={"key": CAPTCHA_API_KEY, "method": "post"},
                files={"file": ("captcha.png", image_bytes, "image/png")},
                timeout=30
            )
            if not r.ok or "OK|" not in r.text:
                return f"[ERROR: {r.text}]"
            cap_id = r.text.split("|",1)[1]
            for _ in range(CAPTCHA_MAX_TRIES):
                time.sleep(CAPTCHA_POLL_SEC)
                rr = requests.get("http://rucaptcha.com/res.php",
                                  params={"key": CAPTCHA_API_KEY, "action": "get", "id": cap_id},
                                  timeout=30)
                if rr.text.startswith("OK|"):
                    return rr.text.split("|",1)[1]
                if rr.text in ("CAPCHA_NOT_READY","CAPTCHA_NOT_READY"):
                    continue
                return f"[ERROR: {rr.text}]"
            return "[TIMEOUT]"
        except Exception as e:
            return f"[ERROR: {e}]"
