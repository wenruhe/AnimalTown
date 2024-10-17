# 事件模板，用于匹配和推导潜在事件
EVENT_TEMPLATES = {
    "build": ["Bridge Building", "House Construction", "Farm Creation"],
    "repair": ["Bridge Repair", "House Repair", "Farm Maintenance"],
    "collaborate": ["Teamwork Project", "Group Task"],
    "celebrate": ["Festival Preparation", "Party Planning"]
}

# 从信件中自动提取事件名称的函数
def extract_event_from_letter(letter_content):
    # 使用正则表达式从信件中提取关键动词
    action_keywords = re.findall(r"\b(build|repair|collaborate|celebrate|organize)\b", letter_content.lower())
    if action_keywords:
        # 如果找到关键动词，根据模板返回可能的事件名称
        possible_events = []
        for action in action_keywords:
            if action in EVENT_TEMPLATES:
                possible_events.extend(EVENT_TEMPLATES[action])
        return possible_events
    else:
        return []

# GPT function call for event suggestion based on letter content when no event is directly mentioned
def gpt_infer_event_from_context(animal_name, letter_content):
    prompt = f"""
    The mayor of Animal Town has sent a letter to {animal_name}. The letter says:
    "{letter_content}"

    The letter does not explicitly mention an event, but based on the letter's content, what events might {animal_name} suggest or initiate? Provide some possible events that make sense in this context.
    """
    
    # Simulate GPT-based inference (simplified for example)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # 假设GPT返回可能的事件名称列表
    possible_events = response['choices'][0]['message']['content'].split(", ")
    return possible_events

# 全部结合的事件触发逻辑：从信件中获取事件，或通过GPT推测
def determine_event_from_letter(animal_name, letter_content):
    # 1. 尝试从信件内容中提取事件名称
    possible_events = extract_event_from_letter(letter_content)
    
    # 2. 如果提取不到，调用 GPT 进行推断
    if not possible_events:
        print("No explicit events mentioned, inferring possible events from context...")
        possible_events = gpt_infer_event_from_context(animal_name, letter_content)
    
    # 如果成功获取到事件，返回事件名称，否则返回无事件
    if possible_events:
        print(f"Possible events extracted or inferred: {possible_events}")
        return possible_events
    else:
        print("No events could be inferred.")
        return None
