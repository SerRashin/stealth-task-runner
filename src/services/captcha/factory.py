from typing import Optional
from src.core.config import DEFAULT_CAPTCHA_PROVIDER
from src.services.captcha.base import CaptchaInterface
from src.services.captcha.twocaptcha import TwoCaptchaService
from src.services.captcha.rucaptcha import RuCaptchaService

def get_captcha_service(provider: Optional[str] = None) -> CaptchaInterface:
    name = (provider or DEFAULT_CAPTCHA_PROVIDER or "").lower()
    if name == "rucaptcha":
        return RuCaptchaService()
    return TwoCaptchaService()
