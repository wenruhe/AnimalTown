from abc import ABC, abstractmethod
from datetime import datetime

# 抽象基类 Memory
class Memory(ABC):
    def __init__(self):
        self.daily_memory = {}  # 平日记忆
        self.overall_memory = []  # 整体记忆
    
    # 添加平日记忆
    @abstractmethod
    def add_daily_memory(self):
        pass
    # 拼凑平日记忆到整体记忆
    @abstractmethod
    def consolidate_memory(self):
        pass

    # 记录完成事件的抽象方法
    @abstractmethod
    def add_finished_event(self, event: str, details: str):
        pass

    # 每日遗忘机制的抽象方法
    @abstractmethod
    def forget(self):
        pass

# # 游戏历史记忆类
# class GameHistoryMemory(Memory):
#     def __init__(self):
#         super().__init__()
#         self.festivals = []  # 节日记忆
#         self.game_progress = {}  # 游戏进度
    
#     # 添加每日记忆
#     def add_daily_memory(self, summary: str):
#         today = datetime.now().date()
#         self.daily_memory[today] = summary
    
#     # 记录游戏完成事件
#     def add_finished_event(self, event: str, details: str):
#         self.overall_memory.append({"event": event, "details": details})
    
#     # 拼凑每日记忆到整体记忆
#     def consolidate_memory(self):
#         for day, summary in self.daily_memory.items():
#             self.overall_memory.append({"day": day, "summary": summary})
    
#     # 遗忘机制
#     def forget(self):
#         if len(self.daily_memory) > 30:  # 保留最近30天的游戏历史
#             oldest_day = min(self.daily_memory.keys())
#             del self.daily_memory[oldest_day]