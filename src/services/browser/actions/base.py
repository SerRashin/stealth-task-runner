from abc import ABC, abstractmethod

class ActionInterface(ABC):
    @abstractmethod
    def supports(self, type_str: str) -> bool: ...
    @abstractmethod
    def execute(self, driver, wins, step, job, res) -> None: ...
