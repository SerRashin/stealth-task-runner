from pydantic import BaseModel
import typing as t

class Action(BaseModel):
    type: str
    action: dict
    target: t.Optional[str] = None  # window alias
