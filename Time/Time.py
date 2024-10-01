
class TimeSystem:
    def __init__(self):

        self.DAYS_IN_YEAR = 120   # 每年有120天（假设每季30天）
        self.DAYS_IN_SEASON = 30  # 每个季节有30天
        self.SEASONS = ["Spring", "Summer", "Autumn", "Winter"]
        self.HOURS_IN_DAY = 24    # 一天有24小时
        self.current_season = self.SEASONS[0]
        self.current_day = 1      # 游戏从第1天开始
        self.current_year = 1     # 第1年
        self.day_of_season = 1    # 季节中的第1天
        self.current_time = 9     # 早晨9点开始
    

    def _get_time(self):
        return (f'{self.current_year} year, {self.current_season} season, {self.current_day} day, {self.current_time} time')

    # 推移时间线，接受小时、天数或年数
    def advance_time(self,**kwargs):
        # Convert all time units to hours
        hours = kwargs.get('hours', 0)
        days = kwargs.get('days', 0)
        years = kwargs.get('years', 0)

        total_hours_passed = (
            years * self.DAYS_IN_YEAR * self.HOURS_IN_DAY +
            days * self.HOURS_IN_DAY +
            hours
        )

        # Update the current time and calculate extra days if any
        total_days_passed = total_hours_passed // self.HOURS_IN_DAY
        remaining_hours = total_hours_passed % self.HOURS_IN_DAY

        self.current_time += remaining_hours
        if self.current_time >= self.HOURS_IN_DAY:
            self.current_time -= self.HOURS_IN_DAY
            total_days_passed += 1

        # Calculate the total days since game start
        # First, find the total days into the current year
        current_season_index = self.SEASONS.index(self.current_season)
        days_into_current_season = self.current_day - 1
        days_into_current_year = current_season_index * self.DAYS_IN_SEASON + days_into_current_season

        # Total days since game start
        total_days_since_start = (self.current_year - 1) * self.DAYS_IN_YEAR + days_into_current_year + total_days_passed

        # Update current year
        self.current_year = (total_days_since_start // self.DAYS_IN_YEAR) + 1

        # Days into the current year
        days_into_current_year = total_days_since_start % self.DAYS_IN_YEAR

        # Update current season
        current_season_index = (days_into_current_year) // self.DAYS_IN_SEASON
        self.current_season = self.SEASONS[current_season_index % len(self.SEASONS)]

        # Update current day (day within the season)
        self.current_day = (days_into_current_year % self.DAYS_IN_SEASON) + 1


if __name__ == "__main__":
    time_system = TimeSystem()
    time_system.advance_time(hours=5)
    print(time_system._get_time())
    time_system.advance_time(days=2)
    print(time_system._get_time())
    time_system.advance_time(hours=88, days=125, years=3)
    print(time_system._get_time())