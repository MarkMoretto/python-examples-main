
"""
Purpose: Stackoverflow solution
Date created: 2020-07-16

Question: https://stackoverflow.com/questions/62936243/combine-regex-searches-into-one-match/62936639#62936639

Contributor(s):
    Mark M.
"""



import re


demo = "Name Klein Vorname Marvin"

pattern = r"""
    Name                # Specific string
    \s+?                # One or more whitespaces
    (?P<last>[\w]+)     # Tagged group 'first'
    \s+?                # One or more whitespaces
    Vorname             # Specific string
    \s+?                # One or more whitespaces
    (?P<first>[\w]+)    # Tagged group 'last'
    """

res = re.search(pattern, demo, flags = re.X | re.I)
res.group("last")
res.group("first")

" ".join([res.group("first"), res.group("last")])
" ".join([res.group(2), res.group(1)])


pattern2 = r"""
    (?:[\w]+)           # Skip the first string ('Name')
    \s+?                # One or more whitespaces
    (?P<last>[\w]+)     # Tagged group 'first'
    \s+?                # One or more whitespaces
    (?:[\w]+)           # Skip the second string ('Vorname')
    \s+?                # One or more whitespaces
    (?P<first>[\w]+)    # Tagged group 'last'
    """

res = re.search(pattern2, demo, flags = re.X | re.I)
res.group("last")
res.group("first")



(?:[\w]+)\s+?(?P<last>[\w]+)\s+?(?:[\w]+)\s+?(?P<first>[\w]+)
