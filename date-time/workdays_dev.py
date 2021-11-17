
"""
Purpose: Datetime + Calendar work
Date created: 2021-11-02

Contributor(s):
    Mark M.

https://www.timeanddate.com/holidays/us/2021   
"""

import calendar
import urllib.request as ureq
from datetime import (
        datetime as dt,
        date,
        timedelta as td
        )

today: dt = dt.now()
WORKING_DAYS_PER_YEAR: int = 251
WEEKEND_WEEKDAY_NUMS: tuple = 5, 6
CURRENT_YEAR: int = today.year
NEXT_YEAR: int = today.year + 1



class DateItem:
    __slots__ = ["calendar_date", "is_holiday", "is_weekend"]
    def __init__(self, calendar_date: dt.date, is_holiday: bool = False, is_weekend: bool = False):
        self.calendar_date = calendar_date
        self.is_holiday = is_holiday
        self.is_weekend = is_weekend

    @property
    def is_workday(self) -> bool:
        return not (self.is_holiday or self.is_weekend)


def us_holiday_url(year: int = today.year) -> str:
    return f"https://www.timeanddate.com/holidays/us/{year}"


req_obj = ureq.Request(us_holiday_url())
with ureq.urlopen(req_obj) as resp:
    data = resp.read().decode("utf-8")

data = data.decode("utf-8")
lines = [str(line).strip() for line in data.splitlines()]


holidays = dict(
    new_years_day = date(today.year, 1, 1),
    mlk_day = date(today.year, 1, 18),
    presidents_day = date(today.year, 2, 15),
    memorial_day = date(today.year, 5, 31),
    independence_day = date(today.year, 7, 4),
    labor_day = date(today.year, 9, 6),
    colum = date(today.year, 10, 11),
    veter = date(today.year, 11, 11),
    thank = date(today.year, 11, 25),
    xmas = date(today.year, 12,25),
    )
holidays_ext = dict(
    nye = date(today.year, 1, 1),
    mlk = date(today.year, 1, 18),
    prez = date(today.year, 2, 15),
    memor = date(today.year, 5, 31),
    indep = date(today.year, 7, 4),
    labor = date(today.year, 9, 6),
    colum = date(today.year, 10, 11),
    veter = date(today.year, 11, 11),
    thank = date(today.year, 11, 25),
    xmas_eve = date(today.year, 12, 24),
    nye = date(today.year, 12, 31),
    )

# start_dt = date(today.year, 1, 1)
# stop_dt = date(today.year + 1, 1, 1)
# net_days = (stop_dt - start_dt).days


cal = calendar.Calendar()
MONTH_NUMBER: int = 11

day_list = []
iter_dates = cal.itermonthdates(today.year, MONTH_NUMBER)
for _dt in iter_dates:
    if _dt.month == MONTH_NUMBER:
        _dt_item = DateItem(_dt)
        _dt_item.is_holiday = True if _dt in holidays.values() else False
        _dt_item.is_weekend = True if _dt.weekday() in WEEKEND_WEEKDAY_NUMS else False
        day_list.append(_dt_item)

# Test index
# For November 2021, index 24 corresponds to Thanksgiving Day.
SAMPLE_DAY_INDEX: int= 24
day_list[SAMPLE_DAY_INDEX].calendar_date
day_list[SAMPLE_DAY_INDEX].is_holiday
day_list[SAMPLE_DAY_INDEX].is_weekend
day_list[SAMPLE_DAY_INDEX].is_workday
for d in day_list:
    print(d.calendar_date, d.is_workday)
