from pydantic import BaseModel, Field
import uuid
from typing import Literal, List
from db.userConfigs import user_credentials

class Animal(BaseModel):
    userID: str = user_credentials.USERID # 和用户账户相关联
    animalID: str = Field(default_factory=lambda: str(uuid.uuid4())) # 每个用户下的每个动物拥有一个独立ID
    name: str
    age: int
    gender: Literal['男', '女']
    job: str
    personality: List[str]
    memory: List[str] = []
    relations: List[dict] = []
    self_perception: str # 自我认知/人设:这是角色对“自己是谁”“自己有什么样的性格和行为倾向”的主观认识。用于约束语言模型内部的角色风格和推理方式。eg.“他不擅长表达情绪，也害怕成为众人关注的焦点。”
    profile: str # 这是一个更“外显”的人物设定，往往由外部视角描述，包括他的日常行为、习惯、技能、爱好、外貌等。eg."他总会记住常客的喜好，把货物摆得整整齐齐。"