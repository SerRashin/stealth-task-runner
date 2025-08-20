import importlib, pkgutil
from typing import List, Optional
from src.services.browser.actions.base import ActionInterface

class ActionsRegistry:
    def __init__(self):
        self._handlers: List[ActionInterface] = []
    def register(self, handler: ActionInterface):
        self._handlers.append(handler)
    def find(self, type_str: str) -> Optional[ActionInterface]:
        for h in self._handlers:
            if h.supports(type_str):
                return h
        return None

_registry = ActionsRegistry()

def get_registry() -> ActionsRegistry:
    return _registry

def load_all_handlers():
    pkg = "src.services.browser.actions.impl"
    mod = importlib.import_module(pkg)
    for m in pkgutil.iter_modules(mod.__path__):
        module = importlib.import_module(f"{pkg}.{m.name}")
        if hasattr(module, "handler"):
            _registry.register(getattr(module, "handler"))
