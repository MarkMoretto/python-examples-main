

"""
Purpose: Extract hours and minutes from dataframe.
Date: 2019-05-04


URL: https://stackoverflow.com/questions/55984986/python-evaluate-arithmetic-string-within-pandas-dataframe-column/55985223#55985223
"""

import re
import pandas as pd

### Sample data value
tst = '1 Hour 5 Minutes'

### Using standard functions to clean and calculate.
tst_hour = int(tst.split('Hour')[0].strip()) * 60
tst_min = int(tst.split('Hour')[1].replace('Minutes', '').strip())
tot_time = tst_hour + tst_min



# using regular expressions
ddict = {
    'Record': [1, 2, 3, 4],
    'Duration': ['1 Hour 5 Minutes',
                 '2 Hours 1 Minute',
                 '2 Hours 45 Minutes',
                 '7 Minutes']
    }

df = pd.DataFrame(ddict)


### Replace plurals in 'Duration' using regular expression option in pandas.Series.replace()
df['Duration'] = df['Duration'].replace(r'Hours', 'Hour', regex=True).replace(r'Minutes', 'Minute', regex=True)

### Iterate the dataframe index; Check if 'Hour' in 'Duration' value for each row; Calculate total time
for i in df.index:
    if 'Hour' in df['Duration'][i]:
        df.loc[i, 'Duration'] = (int(df['Duration'][i].split('Hour')[0].strip()) * 60) + int(df['Duration'][i].split('Hour')[1].replace('Minute', '').strip())
    else:
        df.loc[i, 'Duration'] = int(df['Duration'][i].split('Minute')[0].strip())


##############################################################################################
# using regular expressions
p = re.compile(r'(\d)\s+Hour\w?\s+(\d)\sMinute\w?\s?')
#m = p.match(df['Duration'][0])
#m.group(1)
#m.group(2)

for i in df['Duration']:
    m = p.match(i)
    try:
        (int(m.group(1)) * 60) + int(m.group(2))
    except (re.error, ValueError):
        pass

### Expand values into new columns with labelled headers.

df['Duration'].str.extract(r'(?P<Hours>\d+)\s+?Hour[s]?\s+?(?P<Minutes>\d+)\s+?Minute[s]?', expand=True)
