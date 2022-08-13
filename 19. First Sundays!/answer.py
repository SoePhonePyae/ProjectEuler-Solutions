'''January 1st 1900 is a Monday. add 365 and get a modulo of it with 7 will get
1 which mean January 1st 1901 is a Tuesday. We use this information and get a
tick everytimes the modulo is equal to 5, which is a sunday.'''

import calendar
total_days = 0
total_sunday = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        days = calendar.monthrange(year, month)[1]
        total_days += days
        if total_days % 7 == 5:
            total_sunday += 1

print(total_sunday)
