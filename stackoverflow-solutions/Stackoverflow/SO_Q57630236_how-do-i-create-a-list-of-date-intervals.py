
"""
Purpose: Stackoverflow question on getting a list of dates between two dates.
Date created: 2019-08-23

Contributor(s):
    Mark M.

Ref: https://stackoverflow.com/questions/57630236/how-do-i-create-a-list-of-date-intervals-in-python/57630469#57630469
"""



import datetime as dt
max_start_date = '2017-01-01'
max_end_date = '2017-12-31'


def dt_range(*args):
    dt_start = dt.datetime.strptime(args[0], '%Y-%m-%d')
    dt_end = dt.datetime.strptime(args[1], '%Y-%m-%d')
    for i in range(int((dt_end - dt_start).days)+1):
        yield dt_start + dt.timedelta(i)


for i in dt_range(max_start_date, max_end_date):
    print(i.strftime('%Y-%m-%d'))

max_start_date = '2017-02-01'
max_end_date = '2017-03-03'

for i in dt_range(max_start_date, max_end_date):
    print(i.strftime('%Y-%m-%d'))
