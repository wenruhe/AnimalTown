from typing import List, Optional


class Job:
    def __init__(self, name:str, description:str, impact_areas: List[str], required_resources=Optional[list], provided_services=Optional[list]):
        self.name = name
        self.description = description
        self.impact_areas = impact_areas
        self.required_resources = required_resources
        self.provided_services = provided_services
    
    def add_required_resource(self, resources):
        for resource in resources:
            self.required_resources.append(resource)
    
    def add_provided_service(self, service):
        self.provided_services.append(service)
    
    def trigger_event(self):
        # 这里可以根据职业触发特定的事件
        print(f"{self.name}职业触发了一个事件！")

    def _display_info(self):
        print(f"职业名称: {self.name}")
        print(f"职责描述: {self.description}")
        print(f"影响领域: {', '.join(self.impact_areas)}")
        print(f"所需资源: {', '.join(self.required_resources)}")
        print(f"提供的服务: {', '.join(self.provided_services)}")

 