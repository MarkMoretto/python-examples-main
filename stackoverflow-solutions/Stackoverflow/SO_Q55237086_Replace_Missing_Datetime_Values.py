
"""
Reference Stackoverflow question:
    https://stackoverflow.com/questions/55237086/how-to-replace-missing-date-from-nat-to-some-date-in-increasing-order-in-python

"""

import pandas as pd
import datetime as dt

ddict = {
    'Date': ['2014-12-29','2014-12-30','2014-12-31','','','','',]
    }

data = pd.DataFrame(ddict)
data['Date'] = pd.to_datetime(data['Date'])

def fill_dates(data_frame, date_col='Date'):
    ### Seconds in a day (3600 seconds per hour x 24 hours per day)
    day_s = 3600 * 24

    ### Create datetime variable for adding 1 day
    _day = dt.timedelta(seconds=day_s)

    ### Get the max non-null date
    max_dt = data_frame[date_col].max()

    ### Get index of missing date values
    NaT_index = data_frame[data_frame[date_col].isnull()].index

    ### Loop through index; Set incremental date value; Increment variable by 1 day
    for i in NaT_index:
        data_frame[date_col][i] = max_dt + _day
        _day += dt.timedelta(seconds=day_s)

### Execute function
fill_dates(data, 'Date')