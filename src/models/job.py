from pydantic import BaseModel
import typing as t
from src.models.context import Context
from src.models.action import Action

class Job(BaseModel):
    url: str
    context: Context = Context()
    vars: dict = {}
    actions: t.List[Action]
    return_: dict = {}
