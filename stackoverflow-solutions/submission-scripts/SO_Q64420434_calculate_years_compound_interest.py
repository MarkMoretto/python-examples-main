
"""
Purpose: Finding years in compounding formula.
Date created: 2020-10-18

https://stackoverflow.com/questions/64420434/calculate-years-compound-interest-python/64420535#64420535

Contributor(s):
    Mark M.
"""

from math import log

p_start = 1500
rate = 4.3
p_end = 2000


"""
# Breakdown
round((
       log(A / P) /
       (n * (
               log(1 + (r/n))
               )
        )
    ) + 0.5 # Add 0.5 to account for needing to round up.
, 0) # Round to zero decimal places
"""
get_time = lambda A, P, r, n=12: round((log(A / P) / (n * (log(1 + (r/n)))))+0.5,0)


get_time = lambda A, P, r, n=12: round((xlog(A / P) / (n * (xlog(1 + (r/n)))))+0.5,0)

if r > 0:
    r /= 100

get_time(p_end, p_start, r, 1)

############### Solution for added commentary.
import math

def calculate_years_to_target(principal, rate, target, n=12):

    if rate > 0:
        rate /= 100

    years = round((math.log(target / principal) / (n * (math.log(1 + (rate/n))))) + 0.5, 0)
    return years

calculate_years_to_target(p_end, p_start, r, 1)