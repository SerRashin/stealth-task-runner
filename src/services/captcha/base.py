from abc import ABC, abstractmethod

class CaptchaInterface(ABC):
    @abstractmethod
    def solve(self, image_bytes: bytes) -> str:
        """Return solved text or error marker."""
