from typing import Literal, Optional

class Festival:
    def __init__(self, 
                 name:str, 
                 season:int, 
                 day:int, 
                 year:Optional[int], 
                 duration:int,
                 description:str) -> None: 
        self.name = name
        self.season = season
        self.day = day
        self.year = year
        self.how_often = Literal['daily', 'weekly', 'monthly', 'yearly', 'bi-yearly'] # 这个暂时还不知道有啥用
        self.duration = duration
        self.description = description


    def __str__(self):
        return f"{self.name} on {self.season} {self.day}"

planting_festival = Festival('植树节', 0, 10, description="镇上每年都会举办植树节，动物居民会参与在公共区域种植树木和花卉，象征新的开始和环境保护。")
spring_feast_festival = Festival('春日盛宴', 0, 30, duration=3)
