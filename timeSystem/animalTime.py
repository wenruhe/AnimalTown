from pydantic import BaseModel, Field
from typing import Optional, List
from timeSystem.festivals import Festival



class TimeDuration(BaseModel):
    """
    一个时间段class，如果不给出参数则为0
    """
    hours: int = Field(0, ge=0)  # 确保 hours 为非负整数
    days: int = Field(0, ge=0)   # 确保 days 为非负整数
    years: int = Field(0, ge=0)  # 确保 years 为非负整数


class AnimalTime(BaseModel):
    """
    一个时间点class，如果不给出参数，则默认游戏开始时间点
    """
    time: int = Field(0, ge=0, le=23, description="当前小时")  # 时间默认从 0 点开始，非负整数
    day: int = Field(1, ge=1, le=30, description="当前天数")  # 默认从第 1 天开始
    season_idx: int = Field(0, ge=0, le=3, description="当前季节索引")  # 季节从 0-3 (春-冬)
    year: int = Field(1, ge=1, description="当前年份")  # 默认从第 1 年开始

    HOURS_IN_DAY: int = 24
    DAYS_IN_SEASON: int = 30
    DAYS_IN_YEAR: int = 120
    SEASONS: list = ["春季", "夏季", "秋季", "冬季"]

    def __str__(self) -> str:
        return f"{self.time}点，{self.SEASONS[self.season_idx]}第{self.day}天，第{self.year}年"


    def advance_time(self, duration:TimeDuration):
        """
        take in 一个time period，更新当前自身时间点为 + time period后的时间点
        """
        hours = duration.hours
        days = duration.days
        years = duration.years

        total_hours = (
            years * self.DAYS_IN_YEAR * self.HOURS_IN_DAY +
            days * self.HOURS_IN_DAY +
            hours
        )

        self.time += total_hours % self.HOURS_IN_DAY
        extra_days = total_hours // self.HOURS_IN_DAY

        # 如果小时数超过了一天，调整小时并增加一天
        if self.time >= self.HOURS_IN_DAY:
            self.time -= self.HOURS_IN_DAY
            extra_days += 1

        # 更新天数，并计算需要增加的季节数
        self.day += extra_days
        extra_seasons = 0
        while self.day > self.DAYS_IN_SEASON:
            self.day -= self.DAYS_IN_SEASON
            extra_seasons += 1

        # 更新季节，并计算需要增加的年数
        self.season_idx += extra_seasons
        extra_years = 0
        while self.season_idx >= len(self.SEASONS):
            self.season_idx -= len(self.SEASONS)
            extra_years += 1

        # 更新年份
        self.year += extra_years
    
    def is_later_than(self, another_time: "AnimalTime") -> bool: ## 这里用了前向引用！tmd我也不知道为啥这样能行，但是another_time是一个Time object！！！？？
        if self.year != another_time.year:
            return self.year > another_time.year
        if self.season_idx != another_time.season_idx:
            return self.season_idx > another_time.season_idx
        if self.day != another_time.day:
            return self.day > another_time.day
        if self.time != another_time.time:
            return self.time > another_time.time
        return False


class Calendar(BaseModel):
    cur_time: AnimalTime = AnimalTime()
    # festival_list: List[Festival] = []

    # TODO: 生成初始节日
    def _init_festivals(self):
        pass
    
    
    # TODO: 查看今天有什么节日
    def check_today() -> List[Festival]:
        pass


if __name__ == "__main__":
    calendar = Calendar() # calendar 当前时间为 0点，春季第1天，第1年
    time1 = AnimalTime() # time1 当前时间为 0点，春季第1天，第1年
    time1.advance_time(TimeDuration(years=2)) # time1 当前时间为 0点，春季第1天，第3年
    print(time1)
    calendar.cur_time.advance_time(TimeDuration(hours=999)) # calendar 当前时间为 15点，夏季季节第12天，第1年
    print(calendar.cur_time)
    print(calendar.cur_time.is_later_than(time1)) # false