# special_method.py

import datetime
from datetime import date

MESSAGES_PER_DAY = 100

def divmod(num_rows, messages_per_day):
    """

    Parameters
    ----------
    num_rows: int, number of rows in the input file
    messages_per_day: int, messages received per day

    Returns
    -------
    days, index

    """
    index = 10  # default of 10 will cause an assertion error if the condition below is bypassed for some strange reason
    days = int(num_rows / messages_per_day)
    if num_rows % messages_per_day == 0:
        index = 0
    elif num_rows % messages_per_day > 0:
        index = 1

    return days, index


class SpecialMethod:
    """
    start date format: string of mon/day/year

    """

    def __init__(self, start_date, num_rows):
        self.start_date = date.fromisoformat(start_date)
        self.index = 0
        self.num_rows = num_rows

    def next_date(self):
        days, index = divmod(num_rows=self.num_rows, messages_per_day=MESSAGES_PER_DAY)
        s = self.start_date
        when = (datetime.datetime(s.year, s.month, s.day)
                + datetime.timedelta(days=days))
        assert index in {0, 1}, index
        if index == 0:
            offset = datetime.timedelta(hours=9)
        else:
            offset = datetime.timedelta(hours=14)

        return when + offset


special = SpecialMethod('1978-04-23', 230)

print(f"start date = {special.start_date}")

print(f"next date = {special.next_date()}")
