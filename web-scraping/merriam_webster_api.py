
"""
Purpose: 
Date created: 2020-03-13

Contributor(s):
    Mark M.
"""

import re
from urllib.request import urlopen

keyword = "gathering"

core_url = "https://www.merriam-webster.com"
url_type = ["dictionary","thesaurus",]

def url_join(x,y):
    return f"{x}/{y}"

dict_url = url_join(core_url, url_type[0])
thes_url = url_join(core_url, url_type[1])

with urlopen(url_join(dict_url, keyword)) as resp:
    data = resp.read().decode("utf-8")


tst1 = '<a href="/dictionary/assembly" class="mw_t_sx"><span class="text-uppercase">assembly</span></a>'

# def_ptrn = rb'<span\s+?class\="dt\s*?">(.+)<ul>'
# def_ptrn = r"""
#     <a\shref\="\/\w+\/\w+"\sclass\="mw_t_\w+?">
#     (?:<span\s.+>)?
#     (.+)
#     (?:<\/span>)?
#     <\/a>
#     """

def_ptrn = r'<(?:\w+)\sclass\="mw_t_\w{1,2}">(.+)<\/\\1>'
p = re.compile(def_ptrn, flags = re.M)
p.findall(data)

