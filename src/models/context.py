from pydantic import BaseModel
import typing as t

class Context(BaseModel):
    headless: bool = True
    timeout_sec: int = 40
    locale: str = "ru-RU"
    user_agent: t.Optional[str] = None
    proxy: t.Optional[str] = None
    viewport: dict = {"width": 1366, "height": 768}
    cookies: t.List[dict] = []
