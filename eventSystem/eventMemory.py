from datetime import datetime
from Animals.relation import Relationships
import openai
import re
from animalEvent import Event
class EventMemory:
    def __init__(self, Event):
        self.event_logs = []  # 事件的详细日志
        self.completed = False  # 事件是否完成
    
    # 开始记录事件
    def start_event(self, animals: list, environment_effects: dict):
        self.start_time = datetime.now()
        self.involved_animals = {animal: {"relationship_changes": {}, "mood": "neutral"} for animal in animals}
        self.environment_effects = environment_effects
        self.event_logs.append(f"Event '{self.event_name}' started with animals: {', '.join(animals)}.")

    # 记录事件进程中的日志
    def log_event(self, description):
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.event_logs.append(f"[{log_time}] {description}")
    
    # 完成事件，记录持续时间并总结事件
    def complete_event(self, outcome):
        self.end_time = datetime.now()
        self.duration = (self.end_time - self.start_time).total_seconds()
        self.completed = True
        self.event_logs.append(f"Event '{self.event_name}' completed. Outcome: {outcome}. Duration: {self.duration:.2f} seconds.")
    
    # LLM 生成事件总结
    def llm_generate_event_summary(self):
        summary_prompt = f"""
        你是事件管理者。请根据事件 '{self.event_name}' 的日志，生成一段总结。总结应包括事件的主要过程、参与的动物、环境变化、以及动物关系的变化。
        """
        # 这里调用LLM函数，简化为示例函数调用
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": summary_prompt}
            ]
        )
        
        # 获取 GPT 返回的事件建议
        summary = response['choices'][0]['message']['content']
        return summary
    
    # LLM 分析事件中的关系变化
    def llm_analyze_relationship_changes(self):
        relationship_prompt = f"""
        你是事件管理者。请根据事件 '{self.event_name}' 的日志，分析动物之间关系的变化，并生成一段总结。分析应包括哪些关系得到改善，哪些关系恶化。relation的格式定义如下：
        {
            "animal_1": "Animal1",
            "animal_2": "Animal2",
            "relation": "Friendship",
            "value_change": 10 #通过这个字段来表示关系的变化，正数表示关系变好，负数表示关系变坏,数值定义在-10到10之间
            }，请在回复的最后返回这样json格式的relation

        """
        # 调用LLM函数
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": relationship_prompt}
            ]
        )
        
        relationship_analysis = response['choices'][0]['message']['content']
        
        #正则匹配到json格式的relation并解析成changes
        changes = re.findall(r'\{"animal_1": "(.*?)", "animal_2": "(.*?)", "relation": "(.*?)", "value_change": (.*?)\}', relationship_analysis)
        
        return relationship_analysis, changes
    
    # 整合事件记忆：将事件记录合并到整体记忆中
    def consolidate_event_memory(self, overall_memory):
        # 将事件日志和总结整合到总体记忆中
        event_summary = self.llm_generate_event_summary()
        overall_memory.append({
            'event_name': self.event_name,
            'duration': self.duration,
            'logs': self.event_logs,
            'summary': event_summary,
            'relationships': self.involved_animals,
            'environment_effects': self.environment_effects
        })
        self.event_logs.append("Event memory consolidated.")

    # 忘却机制：可以设置一定条件（如超过一定时间）后自动删除事件日志
    def forget(self):
        self.event_logs.clear()
        self.involved_animals.clear()
        self.environment_effects.clear()
        print(f"Memory of event '{self.event_name}' has been forgotten.")