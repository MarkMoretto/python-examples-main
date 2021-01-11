
"""
Purpose: SO - Regex special replacement
Date created: 2020-07-02

https://stackoverflow.com/questions/62701732/replace-symbol-before-match-using-regex-in-python

Contributor(s):
    Mark M.
"""


import re

text1 = ('SOME STRING,99,1234 FIRST STREET,9998887777,ABC')
text2 = ('SOME OTHER STRING,56789 SECOND STREET,6665554444,DEF')
text3 = ('ANOTHER STRING,#88,4321 THIRD STREET,3332221111,GHI')

"""
Desired output:

SOME STRING 99,1234 FIRST STREET,9998887777,ABC
SOME OTHER STRING,56789 SECOND STREET,6665554444,DEF
ANOTHER STRING #88,4321 THIRD STREET,3332221111,GHI
"""


"""
User commentary:

    Use regex to find occurrences of 1-5 digits,
    possibly preceded by a symbol,
    that are between two commas and
    not followed by a space and letters,
    then replace by this match without the preceding comma.    
"""


my_pattern = r"""
    (?:,)           # Non-capturing group for single comma.
    (\W?\d{0,5},)   # Capture zero or one non-ascii characters, zero to five numbers, and a comma
"""

p = re.compile(my_pattern, flags = re.X)
p.sub(r" \1", text1)
p.sub(r" \1", text2)
p.sub(r" \1", text3)


