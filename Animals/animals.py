import pydantic
import uuid
from typing import Literal
from memory import Memory

class Animal(pydantic.BaseModel):
    _id: uuid.UUID = pydantic.Field(default_factory=uuid.uuid4)
    name: str
    age: int
    gender: Literal['Female', 'Male']
    job: str
    personality: str
    daily_routine: str
    memory: Memory

    

