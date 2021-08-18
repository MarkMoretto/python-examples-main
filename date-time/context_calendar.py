

import calendar
from datetime import datetime as dt, timedelta as td


class ContextCalendar(calendar.Calendar):
    """Basic calendar.Calendar class, but with the ability to use it
    as a context object.

    See PEP 343 for more: https://www.python.org/dev/peps/pep-0343/

    Example
    --------
    >>> yr = 2021
    >>> mth = 8
    >>> with ContextCalendar() as cal:
    ...     monthdays = [dt.strftime("%Y-%m-%d") for dt in cal.itermonthdates(yr, mth)]
    ...     print("\\n".join(monthdays[:7]))
    2021-07-26
    2021-07-27
    2021-07-28
    2021-07-29
    2021-07-30
    2021-07-31
    2021-08-01
    >>> with ContextCalendar() as cal:
    ...     monthdays = [dt.strftime("%Y-%m-%d") for dt in cal.itermonthdates()]
    ...     print("\\n".join(monthdays[:7]))
    Traceback (most recent call last):
        ...
    TypeError: itermonthdates() missing 2 required positional arguments: 'year' and 'month'    
    """    
    def __init__(self, firstweekday=0):
        super().__init__(firstweekday)

    def __del__(self):
        del self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        del self
        return

if __name__ == "__main__"
    import doctest
    doctest.testmod()
    
