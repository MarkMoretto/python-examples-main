"""
Purpose: 
Date created: 2020-02-07

Contributor(s):
    Mark M.
"""

import re
import zipfile
from io import BytesIO
import urllib.request as ureq


SOFTWARE_YEAR = 2020


class UnnecessaryClass:

    HREF_PAT = r'<a href\="(.+?)">.*\bModel\b\s+?\bSoftware\b\s+?.*<\/a>'

    def __init__(self, software_year = 2020):
        self.software_year = f"{software_year}"
        self.cms_base_uri = "https://www.cms.gov"

    def __set_uris(self):
        self.__cms_software_uri = ureq.urljoin(
                self.cms_base_uri, \
                "Medicare/Health-Plans/MedicareAdvtgSpecRateStats/Risk-Adjustors")
        self.__software_page = self.__cms_software_uri \
                                + f"-Items/Risk{self.software_year}"

    def run(self):
        self.__set_uris()
        self.match_list = list()

        with ureq.urlopen(self.__software_page) as f:
            raw_data = f.read().decode("utf-8")
        
        ### Tokenize each line; Strip of whitespace; Skip blank lines.
        tokens = [i.strip() for i in raw_data.split("\n") if len(i) > 0]

        ### Compile regular expression.
        p = re.compile(self.HREF_PAT, flags = re.DOTALL)
        p.search(raw_data)

        for tkn in tokens:
            res = p.search(tkn)
            if res:
                self.match_list.append(res.group(1))
        if len(self.match_list) == 1:
            self.zip_uri = ureq.urljoin(self.cms_base_uri, self.match_list[0])
        else:
            print("Multiple matches found! Please check match_list and rerun.")

uc = UnnecessaryClass(SOFTWARE_YEAR)
uc.run()
# uc.zip_uri -> '/files/zip/YYYY-model-software.zip'

RxHCC_PAT = r"\bRxHCC\b\s+?\bsoftware\b\s+?\w+?\d+?\.\d+?\.\w\d\.zip"

with ureq.urlopen(uc.zip_uri) as resp:
    zf = zipfile.ZipFile(BytesIO(resp.read()))


agesex_pat = r"AGESEXV\d+?\.TXT"
for fn in zf.namelist():
    if re.match(RxHCC_PAT, fn):
        with zf.open(fn) as zf2:
            zf2_data = BytesIO(zf2.read())
            with zipfile.ZipFile(zf2_data) as zfn:
                 for f in zfn.namelist():
                     if re.match(agesex_pat, f):
                         with zfn.open(f) as finf:
                             raw_data = finf.read()

zf.close()
