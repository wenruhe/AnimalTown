import time

class Event:
    def __init__(self, trigger_condition, event_name, involved_animals, suggested_by, environment_effects=None):
        self.trigger_condition = trigger_condition  # 事件触发条件
        self.event_name = event_name  # 事件名称
        self.involved_animals = involved_animals  # 涉及的动物
        self.suggested_by = suggested_by  # 提议者
        self.start_time = None  # 事件开始时间
        self.end_time = None  # 事件结束时间
        self.duration = None  # 事件持续时间
        self.event_status = "pending"  # 事件状态: "pending", "in_progress", "completed"
        self.event_outcome = None  # 事件结果
        self.memory_record = []  # 用于记录事件对记忆系统的影响
        self.environment_effects = environment_effects if environment_effects else {}  # 环境变化
        self.relationship_changes = {}  # 动物之间关系的变化

    
    def trigger(self):
        if self.trigger_condition():
            self.start_time = time.time()
            self.event_status = "in_progress"
            print(f"Event '{self.event_name}' started!")
        else:
            print(f"Trigger condition for '{self.event_name}' not met.")
            
    def add_involved_animal(self, animal):
        """增加参与事件的动物"""
        if animal not in self.involved_animals:
            self.involved_animals.append(animal)
            print(f"{animal} has joined the event '{self.event_name}'.")
    # 更新动物之间的关系变化
    def update_relationships(self, animal_1, animal_2, change: dict):
        relationships = Relationships()
        relationships.update_relationship_bidirectional(animal_1, animal_2, change)
        # if animal_1 in self.involved_animals:
        #     self.involved_animals[animal_1]["relationship_changes"][animal_2] = change
        # if animal_2 in self.involved_animals:
        #     self.involved_animals[animal_2]["relationship_changes"][animal_1] = change
        self.event_logs.append(f"Relationship between {animal_1} and {animal_2} changed by {change}.")






