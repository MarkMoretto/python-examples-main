
"""
Purpose: Stakcoverflow question 61353078
Date created: 2020-04-21
URL: https://stackoverflow.com/questions/61353078/python-regex-capture-characters-after-whitespace-and-hyphen/61354480#61354480

Contributor(s):
    Mark M.
"""


# Answer in full text
"""
import re

dt_neg_value = "2020-04-21 23:59:59.999-0400" # Negative UTC
dt_pos_value = "2020-04-21 23:59:59.999+0400" # Positive UTC
dt_london = "2020-04-21 23:59:59.999+00:00" # Zero UTC + colon separator

dt_pat = r'''
    (?P<yr>\d{4})-      # year.  This looks for four numbers.
    (?P<mth>\d{2})-     # month.  This looks for two numbers.
    (?P<dy>\d{2})\s     # day of month.  This looks for two numbers.
    (?P<hh>\d{1,2})     # hour of day.  This looks for one or two numbers.
    :(?P<mm>\d{1,2})    # minute of hour.  This looks for one or two numbers.
    :(?P<nn>\d{1,2})    # second of minute.  This looks for three numbers.
    \.(?P<ms>\d{3})     # millisecond of second.  We have to escape the period so that it doesn't capture a character.
    (?P<utc_off>.?\d+(:\d*)?)  # utc offset. The '-?' part means that a hyphen is optional. This accounts for +/-00:00, as well
    '''

# We'll use re.search passing our patter, variable, and the re.X flag.
# Then we can just call out what we want. I've used `utc_off` to indicate UTC offset.

In[0]: re.search(dt_pat, dt_neg_value, re.X).group("utc_off")
Out[0]: '-0400'

In[1]: re.search(dt_pat, dt_pos_value, re.X).group("utc_off")
Out[1]: '+0400'

In[2]: re.search(dt_pat, dt_london, re.X).group("utc_off")
Out[2]: '+00:00'


If you're ambitious, you can use re.findall() with the same arguments and just pick out
what you want by index.

In[1]: re.findall(dt_pat, dt_neg_value, re.X)
Out[1]: [('2020', '04', '21', '23', '59', '59', '999', '-0400')]


Or, re.search() without all the fuss:

In[2]: re.search(dt_pat, dt_neg_value, re.X).groups()
Out[2]: ('2020', '04', '21', '23', '59', '59', '999', '-0400')


Finally, to keep things in order, try re.match.groupdict()

In[3]: re.match(dt_pat, dt_neg_value, re.X).groupdict()
Out[3]: {'yr': '2020',
    'mth': '04',
    'dy': '21',
    'hh': '23',
    'mm': '59',
    'nn': '59',
    'ms': '999',
    'utc_off': '-0400'}

"""
