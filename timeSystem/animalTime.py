from pydantic import BaseModel, Field
from typing import Optional, List



class TimeDuration(BaseModel):
    """
    一个时间段class，如果不给出参数则为0
    """
    hours: int = Field(0, ge=0)  # 确保 hours 为非负整数
    days: int = Field(0, ge=0)   # 确保 days 为非负整数
    seasons: int = Field(0, ge=0) # 确保 seasons 为非负整数
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


    def advance_time(self, duration: TimeDuration):
        """
        通过传入的 TimeDuration 对象推进时间，更新当前时间点
        """
        # 处理时间的推进：小时、天数、季节、年份
        hours = duration.hours
        days = duration.days
        seasons = duration.seasons
        years = duration.years

        # 1. 处理小时数的推进
        total_hours = hours
        self.time += total_hours % self.HOURS_IN_DAY
        extra_days = total_hours // self.HOURS_IN_DAY

        if self.time >= self.HOURS_IN_DAY:
            self.time -= self.HOURS_IN_DAY
            extra_days += 1

        # 2. 处理天数的推进
        total_days = extra_days + days
        self.day += total_days

        extra_seasons = 0
        while self.day > self.DAYS_IN_SEASON:
            self.day -= self.DAYS_IN_SEASON
            extra_seasons += 1

        # 3. 处理季节的推进
        total_seasons = extra_seasons + seasons
        self.season_idx += total_seasons

        extra_years = 0
        while self.season_idx >= len(self.SEASONS):
            self.season_idx -= len(self.SEASONS)
            extra_years += 1

        # 4. 处理年份的推进
        self.year += extra_years + years
    

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
