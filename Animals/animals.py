from pydantic import BaseModel, PrivateAttr
import uuid
from typing import Literal, List


class Animal(BaseModel):
    _id: uuid.UUID = PrivateAttr(default_factory=uuid.uuid4)
    name: str
    age: int
    gender: Literal['Female', 'Male']
    job: str
    personality: List[str]
    memory: List[str] = []

    

    

