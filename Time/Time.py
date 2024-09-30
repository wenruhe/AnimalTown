

class TimeSystem:
    def __init__(self):

        self.DAYS_IN_YEAR = 120   # 每年有120天（假设每季30天）
        self.DAYS_IN_SEASON = 30  # 每个季节有30天
        self.SEASONS = ["Spring", "Summer", "Autumn", "Winter"]
        self.current_season = self.SEASONS[0]
        self.current_day = 1      # 游戏从第1天开始
        self.current_year = 1     # 第1年
        self.day_of_season = 1    # 季节中的第1天

    def advance_day(self):
        """推进一天，并更新季节和年份"""
        self.current_day += 1
        self.day_of_season += 1
        
        # 如果季节结束，进入下一个季节
        if self.day_of_season > self.days_in_season:
            self.advance_season()
        
        # 检查是否需要更新年份
        if self.current_day > self.days_in_year:
            self.current_year += 1
            self.current_day = 1
            self.current_season = "Spring"
            self.day_of_season = 1
            print(f"Happy New Year! It's now year {self.current_year}")
    
    def advance_season(self):
        """推进季节"""
        current_season_index = self.seasons.index(self.current_season)
        next_season_index = (current_season_index + 1) % len(self.seasons)
        self.current_season = self.seasons[next_season_index]
        self.day_of_season = 1
        print(f"The season has changed! It's now {self.current_season}.")
    
    def check_events(self):
        """检查当天是否有特殊事件或节日"""
        if self.current_season == "Spring" and self.day_of_season == 10:
            print("Today is the Spring Planting Festival!")
            # 执行植树节的相关逻辑
            
        elif self.current_season == "Summer" and self.day_of_season == 15:
            print("The Summer Market is happening today!")
            # 执行夏季集市的相关逻辑
            
        elif self.current_season == "Winter" and self.day_of_season == 1:
            print("Winter Festival starts today!")
            # 执行冬季节日的相关逻辑

        # 可添加更多节日和事件
    def get_time(self):
        return
        
    def get_season(self):
        """返回当前的季节"""
        return self.current_season
    
    def get_day(self):
        """返回当前是第几天"""
        return self.current_day
    
    def get_year(self):
        """返回当前是第几年"""
        return self.current_year
