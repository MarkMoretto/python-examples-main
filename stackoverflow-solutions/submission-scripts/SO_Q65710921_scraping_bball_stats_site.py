
"""
Purpose: Stackoverflow answer
Date created: 2021-01-13
URL: https://stackoverflow.com/questions/65710921/need-assistance-scraping-html-able-from-basketball-reference/65711123?noredirect=1#comment116182533_65711123

Contributor(s):
    Mark M.
"""

import re
from urllib.request import urlopen


url = "https://www.basketball-reference.com/leagues/NBA_2021_games-january.html"

with urlopen(url) as resp:
    data = resp.read().decode("utf-8")


def clean_data(d):
    """Replace newline, tab, and whitespace with single space."""
    return re.sub("\s{2}", " ", re.sub(r"(\t|\n|\s)+", "  ", d.strip()))

# Capture key segments by element tag and string indexing.
tbl_head = data[data.index("<thead"):data.index("</thead>")]
tbl_body = data[data.index("<tbody"):data.index("</tbody>")]

# Clean our head and body data.
tbl_head = clean_data(tbl_head)
tbl_body = clean_data(tbl_body)

# Simple match to get fields from the table.
# \S gets everything besides whitespace.
th_pat = r">(\S+)<"
p = re.compile(th_pat)
fields = p.findall(tbl_head)

# sample = tbl_body[:1000]
# sample = re.sub(r'("|<t\w) >', r'\1>', tbl_body[:1000])
# sample = re.sub(r'>\s+<', '><', sample)

# Creative pattern to capture nested elements.
body_pat = r"""
    <t(?:h|d) .+?>
    (?:<a.+?>)?
    (.*?)
    (?:</a>)?
    </t\w>
    """
p = re.compile(body_pat, flags = re.X) # Use re.X if doing multiline pattern.

p.findall(sample)

# Further cleaning of body data to remove whitespace.
# (Not super necessary.)
body_data = re.sub(r'("|<t\w) >', r'\1>', tbl_body)
body_data = re.sub(r'>\s+<', '><', body_data)

# Replace <tr> tags with newline character.
body_data = re.sub(r'(<tr>|</tr><tr>)', '\n', body_data)

# Iterate each line, capture our pattern output and add it as a sublist to res.
res = []
for line in body_data.split("\n"):
    tmp = p.findall(line)
    if len(tmp) > 0:
        res.append(tmp)

print(f"Number of lines in res: {len(res)}") # Number of lines in res: 238

# First five lines of results
print("\n".join([f"{i}" for i in res[:5]]))



