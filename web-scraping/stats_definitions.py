
"""
Purpose: Scrape stats definitions
Date created: 2020-03-29

Contributor(s):
    Mark M.
"""

import re
import urllib.request as ureq

url = "https://stattrek.com/statistics/dictionary.aspx"
url_qry = "https://stattrek.com/statistics/dictionary.aspx?Definition={term}"

with ureq.urlopen(url) as resp:
    data = resp.read().decode("utf-8")


opt_pat = r'<option value="(.+)">.+?<\/option>'
p = re.compile(opt_pat)
terms = p.findall(data)
terms = [re.sub(r"&#32;", " ", i) for i in terms]

