
"""
Purpose: Stackoverflow response
Date created: 2021-02-09

URL: https://stackoverflow.com/questions/66130408/how-do-i-replace-the-column-headers-in-a-string-with-a-list-of-replacement-colum/66130639#66130639

Contributor(s):
    Mark M.
"""


import re
oldcolumn = '''Table.TransformColumnTypes(#"Promoted Headers",{{"ID_ORD", type text}, {"CDRNOR", type text}, {"DT_ORD", type datetime}, {"FLSTAT", Int64.Type},.....'''
newcolumn = '''CDUNOD   CDTIDO  CDRNOR  DT_ORD....'''
newcolumnList = newcolumn.split()
# originalcolumnsRegex = re.compile(r'\{\"\w+')

ptrn = r'{"([A-Z_]+?)"'
p = re.compile(ptrn)

# p.findall(oldcolumn)


for o, n in zip(p.findall(oldcolumn), newcolumnList):
    oldcolumn = oldcolumn.replace(o, n)



# --- Update with new pattern and method (2021-02-15) --- #

p = re.compile('\{.*?"(?P<mymatch>[A-Z_]+)".+?\}')
# for mtch in p.finditer(oldcolumn): print(mtch.group("mymatch"))

for o, n in zip(p.findall(oldcolumn), newcolumnList):
    oldcolumn = re.sub(rf"{o}", n, oldcolumn, flags=re.I)



# re.sub(ptrn, oldcolumn,)

# for i in newcolumnList
#       originalcolumnsRegex.sub(r'{"'newcolumnList[i],oldcolumn)
#       i = i +1
