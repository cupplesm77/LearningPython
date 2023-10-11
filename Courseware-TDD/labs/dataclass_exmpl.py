from datetime import date, MINYEAR, MAXYEAR
from dataclasses import dataclass

# ********************** NOT @dataclass ***********************


class DateInterval1:
    BEGINNING_OF_TIME = date(MINYEAR, 1, 1)
    END_OF_TIME = date(MAXYEAR, 12, 31)

    def __init__(self, start=None, end=None):
        if start is None:
            start = self.BEGINNING_OF_TIME
        if end is None:
            end = self.END_OF_TIME
        if start > end:
            raise ValueError(f"Start date {start} must not be after end date {end}")
        self.start = start
        self.end = end


# Plus some other methods for checking whether
# a given date is in the interval, et cetera

# **************************** @dataclass *********************************


@dataclass
class DateInterval:
    BEGINNING_OF_TIME = date(MINYEAR, 1, 1)
    END_OF_TIME = date(MAXYEAR, 12, 31)

    start: date = BEGINNING_OF_TIME
    end: date = END_OF_TIME

    def __post_init__(self):
        if self.start > self.end:
            raise ValueError(
                f"Start date {self.start} must not be after end date {self.end}"
            )


#   My Comments:
"""
I re-listened to the Python Dataclass video in OOP:

Advantage of @dataclass
  1) the code is much easier and cleaner...just look at it...10 times easier to read
  2) easier to maintain given only one start and end variables, rather than three times with "self"
  3) therefore, easier to expand in the future
  4) freebies like the __repr__   and other freebies.
  
When to NOT use @dataclass????????
Aaron, That seems like a trick question...

My answer to that question in the words of our venerable mentor from the Data Class video:
  "Use dataclasses in your code.  USE THEM!  Just start writing dataclasses 
  as much as you can..."
   
"""

s1 = date(2023, 10, 1)
e1 = date(2023, 10, 10)
date1 = DateInterval1(s1, e1)

s2 = date(2023, 10, 10)
e2 = date(2023, 10, 1)
date2 = DateInterval(s2, e2)
