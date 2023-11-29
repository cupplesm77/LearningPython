'''

>>> di_all = DateInterval.all()

In the year 3000:

>>> datetime.date(3000, 1, 1) in di_all
True

The last day of 500 AD:

>>> datetime.date(500, 12, 31) in di_all
True

And today:

>>> datetime.date.today() in di_all
True

The 21st century:

>>> di_21st = DateInterval(datetime.date(2000, 1, 1), datetime.date(2099, 12, 31))

>>> datetime.date.today() in di_21st
True

>>> datetime.date(2010, 6, 15) in di_21st
True

>>> datetime.date(1910, 6, 15) in di_21st
False

>>> datetime.date(2040, 2, 7) in di_21st
True

>>> datetime.date(2140, 2, 7) in di_21st
False

First calendar week of the year 2050:

>>> di_firstweek = DateInterval(datetime.date(2050, 1, 2), datetime.date(2050, 1, 8))

Cycling through that week: (look up "f-strings" if you're not familiar
with them already)

>>> for day in di_firstweek:
...     print(f"{day.year}/{day.month:02}/{day.day:02}")
2050/01/02
2050/01/03
2050/01/04
2050/01/05
2050/01/06
2050/01/07
2050/01/08

Checking the defaults:

>>> dt_no_start = DateInterval(None, datetime.date(2100, 1, 1))
>>> dt_no_start.end == DateInterval.END_OF_TIME
False
>>> dt_no_start.start == DateInterval.BEGINNING_OF_TIME
True

>>> dt_no_start = DateInterval(datetime.date(2100, 1, 1), None)
>>> dt_no_start.end == DateInterval.END_OF_TIME
True
>>> dt_no_start.start == DateInterval.BEGINNING_OF_TIME
False

'''

# Write your code here:



# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python. Copyright MigrateUp LLC. All rights reserved.

