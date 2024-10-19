from pydantic import BaseModel, Field
import uuid
from typing import Literal, List
from db.userConfigs import user_credentials
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) ###仅测试时使用
# from eventSystem.animalEvent import AnimalEvent
class Animal(BaseModel):
    #userID: str = user_credentials.USERID
    #animalID: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    age: int
    gender: Literal['Female', 'Male']
    job: str
    personality: List[str]
    memory: List[str] = []
    #动物目前的状态，参与event的创建和设计
    status: Literal['Working', 'Free', 'Boring'] = 'Free'
    idea : dict[str, list[str]] = {'main': [], 'branch': []}
    #动物的行为、能力函数
    def create_event(self, idea, event_name, event_content, involved_animals, suggested_by):
        event_name = f"Event related to {event_name}"
        
        new_event = AnimalEvent(
            trigger_condition=idea,
            event_name=event_name, 
            event_content=event_content, #LLM返回
            involved_animals=involved_animals,
            suggested_by=suggested_by #如果是接受镇长回信，则填写镇长，默认动物自身
        )
        
        return new_event


def deal_main_idea(animal:Animal):
    main_idea_to_event_prompt = "你是动物小镇的idea分析系统，你的任务是根据提供的小动物的状态、性格、当前主要想法给出该小动物可能会发起的活动事件，如：main_idea：修图书馆，status:空闲，则返回 生成事件内容event_content = \"darry现在要去修建图书馆，邀请了好朋友luna\"，event_name = \"修建图书馆\"" ###这个输出后续可以改成function call，返回两个参数，eventcontent和eventname,prompt后续会考虑更多的内容，包括其他动物的参与等等
    animal_provide_main_idea = "我是{animal.name}，目前状态是{animal.status}，性格是{animal.personality}，现在我有这样的想法{animal.idea['main']，branch:[...]，有什么我可以做的呢？"
    # 调用LLM函数
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": main_idea_to_event_prompt},
            {"role": "user", "content": animal_provide_main_idea}
        ]
    )
    
    event_content = response['choices'][0]['message']['content']
    return event_content
    
if __name__ == "__main__":
    darry = Animal(name="Darry", age=23, gender="Male", job="Shopkeeper", personality=["Shy"])
    luna = Animal(name="Luna", age=26, gender="Female", job="Doctor", personality=["Independent", "Smart"])
    
    event = darry.create_event({"main": ["I want to open a shop"],"branch": ['i like work with Luna']}, "修建图书馆", "darry现在要去修建图书馆，邀请了好朋友luna",  [luna], "Darry")
    
    print(event.suggested_by) #Darry
    print(event.involved_animals) 
    #[Animal(name='Luna', age=26, gender='Female', job='Doctor', personality=['Independent', 'Smart'], memory=[], status='Free', idea={'main': [], 'branch': []})]


