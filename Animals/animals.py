from pydantic import BaseModel, Field
import uuid
from typing import Literal, List
from db.userConfigs import user_credentials

class Animal(BaseModel):
    userID: str = user_credentials.USERID # 和用户账户相关联
    animalID: str = Field(default_factory=lambda: str(uuid.uuid4())) # 每个用户下的每个动物拥有一个独立ID
    name: str
    age: int
    gender: Literal['Female', 'Male']
    job: str
    personality: List[str]
    memory: List[str] = []



