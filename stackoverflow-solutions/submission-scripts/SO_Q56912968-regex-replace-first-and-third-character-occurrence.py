
"""
Purpose:


Ref: https://stackoverflow.com/questions/56912968/replace-first-and-third-occurrence-with-another-character-python-regex
"""

import re

sstr = """
gere  should be gara 

cateral    should remain cateral 
"""
regex = r'e(\w+?)e'
new_str = re.sub(regex, r'a\1a', sstr)
print(new_str)



#p = re.compile(regex)
#p.sub('a', sstr, 2)


#re.sub('(a)b', r'\1d', 'abc')
#re.sub(r'(e)\w*?', r'\1a', sstr)