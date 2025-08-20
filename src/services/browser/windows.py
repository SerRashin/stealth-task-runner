from dataclasses import dataclass
import typing as t
from selenium.webdriver import Chrome

@dataclass
class Windows:
    map: dict
    main: str = "main"
    def get(self, alias: t.Optional[str]) -> str:
        return self.map.get(alias or self.main, next(iter(self.map.values())))
    def set(self, alias: str, handle: str):
        self.map[alias] = handle

def switch_to(driver: Chrome, wins: Windows, alias: t.Optional[str]):
    handle = wins.get(alias)
    if driver.current_window_handle != handle:
        driver.switch_to.window(handle)
