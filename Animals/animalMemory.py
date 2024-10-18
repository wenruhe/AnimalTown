from ..memorySystem.memory import Memory
from datetime import datetime

# 动物记忆类
class AnimalMemory(Memory):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.relationships = {}  # 关系值
        self.finished_events = []  # 已完成事件
    
    # 添加平日记忆
    def add_daily_memory(self, daily_logs: list) -> dict:
        today = datetime.now().date()
        daily_memory = {today: daily_logs}
        return daily_memory
    # LLM整合日常记忆
    def llm_generate_daily_exe(self):
        daily_sum_prompt = "你是动物小镇的动物记忆管理者。请根据{animal_name}的日常记忆，生成一段关于今天发生的总结。"
        daily_mood_analyse = "你是动物小镇的动物记忆管理者。请根据{animal_name}的日常记忆，结合行为分析该动物今天与其他动物之间的情绪变化情况，并返回对该动物在情感关系、工作关系上是否有提升或下降。"
        # 调用LLM函数
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": daily_sum_prompt}
            ]
        )
        
        daily_sum = response['choices'][0]['message']['content']
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": daily_mood_analyse}
            ]
        )
        
        analyse = response['choices'][0]['message']['content']
        
        return daily_sum, analyse

    # 记录小动物完成的事件及细节
    def add_finished_event(self, event: str, details: str):
        self.finished_events.append({"event": event, "details": details})
    
    # 遗忘机制：删除过旧的平日记忆
    def forget(self):
        # if len(self.daily_memory) > 7:  # 例如只保留最近7天的记忆
        oldest_day = min(self.daily_memory.keys())
        del self.daily_memory[oldest_day]
        
    # 拼凑平日记忆到整体记忆,整合后调用删除平日记忆函数清理一段时间的平日记忆
    def consolidate_memory(self):
        daily_phase_sum = []
        daily_phase_sum.append(self.daily_memory)
        
        llm_daily_phase_sum = """generate()""" #LLM代入 平日总结、当前需求、当前总体记忆，生成新的总体记忆
        #forget()
        self.overall_memory.append(daily_phase_sum)
    
    

 