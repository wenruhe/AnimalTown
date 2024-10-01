from typing import Literal, Optional, List
from pydantic import BaseModel, Field
from timeSystem.animalTime import AnimalTime, TimeDuration


class Festival(BaseModel):
    """

    表示一个节日，包括下一次发生的时间点、发生频率、持续时间、时间跨度、描述以及总共发生的次数。
    注意！！时间跨度和持续时间不一样！！

    举个例子，奥运会从1900年举办到2900年，每四年举办一次，每次持续10天，则：

    时间跨度为1900年-2900年
    频率为 4 年
    持续时间为 10 天

    """
    name: str  # 节日名称
    next_occurrence: AnimalTime  # 下一次举办的时间点，这个是最重要的！

    time_span_start: AnimalTime = AnimalTime()
    time_span_end: Optional[AnimalTime] = None
    active: bool = True # 通过查看 游戏当前时间 是否在 时间跨度以内 决定是否active，默认为True

    frequency: int = Field(1, ge=1, description="节日举办频率，需要结合frequency_unit一起看，默认为 1 年")  # 举办频率
    frequency_unit: Literal['天', '周', '季', '年'] = Field("年", description="举办频率的单位：周/季/年")  # 举办频率单位
    duration: TimeDuration = TimeDuration(days=1)  # 节日持续时间，默认为1天
    description: str = Field("", description="节日描述")
    occurrences: List[AnimalTime] = []  # 过去举办的时间
    memories: List = [] # TODO: 等memory class写好给festival添加memory，上次这个节日的表现如何


    def __str__(self):
        return self.description
    
    def __len__(self):
        return len(self.occurrences)
    
    def _print_info(self):
        return f"下一次 {self.name} 将在 {self.next_occurrence} 举办。\n 举办频率为 {self.frequency} {self.frequency_unit} 一次。\n 这个节日一共举行了 {self.occurrences_count} 次"
    
    def occur_once(self):
        """
        举办一次，次数+1，更新下一次举办时间
        """
        # 举办次数 + 1
        self.occurrences_count += 1

        # 更新下次举办的时间
        if self.frequency_unit == '天':
            time_duration_ = TimeDuration(days=self.frequency)
        elif self.frequency_unit == '周':
            time_duration_ = TimeDuration(days=self.frequency * 7)
        elif self.frequency == '季':
            time_duration_ = TimeDuration(seasons=self.frequency)
        elif self.frequency == '年':
            time_duration_ = TimeDuration(years=self.frequency)
        self.next_occurrence.advance_time(time_duration_)


        # TODO: 更新这次的节日表现！

        pass

if __name__ == "__main__":
    harvest_festival = Festival(
        name="丰收节", 
        next_occurrence=AnimalTime(day=1, season_idx=2, year=4), 
        description="秋季是丰收的季节，所有农夫都忙于收割作物。镇上的动物们举办了一个庆祝收成的节日，并向镇长（玩家）展示他们的收获。",
        occurrences=[
            AnimalTime(day=10, season_idx=2, year=1),
            AnimalTime(day=10, season_idx=2, year=2),
            AnimalTime(day=10, season_idx=2, year=3)
        ]
    )
    print(len(harvest_festival)) # 3