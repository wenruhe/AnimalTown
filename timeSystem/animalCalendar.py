from pydantic import BaseModel, Field
from typing import Optional, List

from timeSystem.animalTime import AnimalTime, TimeDuration
from timeSystem.festivals import Festival

class AnimalCalendar(BaseModel):
    cur_time: AnimalTime = AnimalTime()
    festival_list: List[Festival] = []

    # TODO: 生成初始节日
    def _init_festivals(self):
        pass
    
    
    # TODO: 查看今天有什么节日
    # def check_today() -> List[Festival]:
        # pass


if __name__ == "__main__":
    calendar = AnimalCalendar() # calendar 当前时间为 0点，春季第1天，第1年
    time1 = AnimalTime() # time1 当前时间为 0点，春季第1天，第1年
    time1.advance_time(TimeDuration(years=2)) # time1 当前时间为 0点，春季第1天，第3年
    print(time1)
    calendar.cur_time.advance_time(TimeDuration(hours=999, days=20, seasons=1)) # calendar 当前时间为 15点，夏季季节第12天，第1年
    print(calendar.cur_time)
    print(calendar.cur_time.is_later_than(time1)) # false