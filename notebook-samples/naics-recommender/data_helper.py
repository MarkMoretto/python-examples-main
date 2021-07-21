
"""
Purpose: 
Date created: 2021-07-19

Contributor(s):
    Mark M.
"""

from io import StringIO
import urllib.parse as upars
import urllib.request as ureq
import orjson
import requests
import pandas as pd


from io import StringIO
import urllib.request as ureq
import orjson
import pandas as pd


base_url = "https://www.census.gov/naics/resources/js/data/naics-sector-descriptions.json"



with ureq.urlopen(base_url) as resp:
    bdata = resp.read()
    # data = StringIO(resp.read().decode("utf-8"))
    if bdata:
        dd = orjson.loads(bdata)


# dd.get("naicsRef")[0].get("table")
# dd.get("naicsRef")[0].get("table").keys()
# dd.get("naicsRef")[0].get("table").get("tableRow")
# orjson.dumps(dd.get("naicsRef"))
# orjson.dumps(dd.get("naicsRef")[0])

df = pd.read_json(orjson.dumps(dd.get("naicsRef")[0].get("table").get("tableRow")))

dfe = df.loc[:, "sectorCode"].str.split("-").explode().reset_index()

pd.merge(dfe, df, how="left", left_on = "sectorCode", right_on = "sectorCode")
pd.merge(dfe, df, how="left", left_index = True, right_index = True)




subsection_base_url = "https://www.census.gov/naics/resources/model/dataHandler.php"
agri_url_sample = "https://www.census.gov/naics/resources/model/dataHandler.php?input=11&chart=2017&search=Y"

qq = upars.urlparse(agri_url_sample)
qq_qry = dict(upars.parse_qsl(qq.query))


argi_subsect_sample = "https://www.census.gov/naics/resources/model/dataHandler.php?=&year=2017&code=11&search=true"

yy = upars.urlparse(argi_subsect_sample)
yy_qry = dict(upars.parse_qsl(yy.query))


code_111111_url = "https://www.census.gov/naics/resources/model/dataHandler.php?=&year=2017&code=11111&search=true"


with ureq.urlopen(base_url) as resp:
    data = StringIO(resp.read().decode("utf-8"))



dfs = pd.read_json(data)

