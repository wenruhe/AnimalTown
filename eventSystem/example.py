# 示例流程：小兔子请求帮助，镇长回信建议事件，兔子决定发起事件
letter_content_with_event = "I suggest you and Fox work together to build a bridge."
letter_content_without_event = "It would be great if you and Fox could find a way to solve the crossing problem together."

# 情景 1: 信件明确提到事件
possible_events_1 = determine_event_from_letter("Bunny", letter_content_with_event)
# 输出应为 ['Bridge Building']

# 情景 2: 信件没有明确提到事件，通过 GPT 推理事件
possible_events_2 = determine_event_from_letter("Bunny", letter_content_without_event)
# GPT 可能推测输出: ['Bridge Building', 'Teamwork Project']

# 创建并触发事件
if possible_events_1:
    event = Event(event_name=possible_events_1[0], involved_animals=["Bunny", "Fox"], suggested_by="Mayor")
    event.trigger()
    event.update_relationship("Bunny", "Fox", 10)  # 更新关系
    event.complete("Bridge successfully built.")
    
    # 记录事件到记忆系统
    event_memory = EventMemory(event_name=event.event_name)
    event_memory.start_event(["Bunny", "Fox"], {"River": "crossable"})
    event_memory.update_relationships("Bunny", "Fox", 10)
    event_memory.complete_event("Bridge successfully built.")
    event_memory.consolidate_event_memory([])  # 整合记忆 

#可能的result
{
  "event_1": {
    "event_name": "Bridge Building",
    "start_time": "2024-10-17 10:11:21.173029",
    "end_time": "2024-10-17 10:11:21.173511",
    "duration": 0.000482,
    "relationships_changes": {
      "Animal1": "Bunny",
      "Animal2": "Fox",
      "relation": "Friendship",
      "value_change": 10
      },
    "status": "completed"
  },  
  "event_2": {
    "event_name": "Bridge Building",
    "start_time": "2024-10-17 10:11:21.173803",
    "end_time": "2024-10-17 10:11:21.173841",
    "relationships_changes": {
      "Animal1": "Bunny",
      "Animal2": "Fox",
      "relation": "Friendship",
      "value_change": -5
      }
    },
    "status": "completed"
}