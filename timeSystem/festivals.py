from typing import Literal, Optional


# class Festival:
#     def __init__(self, 
#                  name:str, 
#                  day:int, 
#                  season_idx:int, 
#                  year:int, 
#                  duration:int, # 持续天数
#                  description:str,
#                  how_often: int,
#                  how_often_unit: Literal['monthly', 'yearly'] = 'yearly',
#                  start_day: tuple = (1, 0, 1), # day 1, spring, year 1
#                  end_day: tuple = (-1, -1, -1) # never ends
#                 ) -> None: 
#         self.SEASONS = ["Spring", "Summer", "Autumn", "Winter"]
#         self.name = name
#         self.season_idx = season_idx
#         self.day = day
#         self.year = year
#         self.how_often = how_often
#         self.how_often_unit = how_often_unit # 这个暂时还不知道有啥用
#         self.duration = duration
#         self.description = description
#         self.occurance = 0

#     # 发生一次，次数+1，update memory，更新下一次发生时间
#     def refresh(self):
#         self.occurance += 1
#         pass

#     def _get_day(self):
#         return self.day, self.season_idx, self.year
    


    # 获取过去节日的表现（记忆）
    def _get_memory(self):
        pass

    def __str__(self):
        return f"{self.name} on {self.day} {self.SEASONS[self.season_idx]} {self.year}; Reoccuring {self.how_often}"
    

spring_festival = Festival("New Year", 
                           day=1, 
                           season_idx=0, 
                           year=1, 
                           duration=3, 
                           description="春节", 
                           how_often=1, 
                           how_often_unit='yearly', 
                           start_day=(10, 0, 1), 
                           end_day=(-1, -1, -1)
                           )
all_festivals = [spring_festival]