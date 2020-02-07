"""
Purpose: 
Date created: 2020-02-07

Contributor(s):
    Mark M.
"""

import re
import zipfile
from os import linesep
from io import BytesIO
import urllib.request as ureq


### We'll target the 2020 software year.
SOFTWARE_YEAR = 2020

class GetZipUrl:
    ### Quick regular expression to parse some raw HTML and get the model
    ### zipfile path.
    HREF_PAT = r'<a href\="(.+?)">.*\bModel\b\s+?\bSoftware\b\s+?.*<\/a>'

    def __init__(self, software_year = 2020):
        self.software_year = f"{software_year}"
        self.cms_base_uri = "https://www.cms.gov"
        self.__cms_software_uri = ureq.urljoin(
                self.cms_base_uri, \
                "Medicare/Health-Plans/MedicareAdvtgSpecRateStats/Risk-Adjustors")
        
    def __set_uri(self):
        """Create additional URIs based on software-year value."""
        self.__software_page = self.__cms_software_uri + f"-Items/Risk{self.software_year}"

    def run(self):
        """Run the class instance."""
        ### Set our URIs
        self.__set_uri()
        
        ### Blank list collection to hold results.
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

            
### Instantiate and run; The zipfile path should be contained within the zip_uri variable.
uc = GetZipUrl(SOFTWARE_YEAR)
uc.run()

### Affirm expected output for 2020
# assert (uc.zip_uri == "/files/zip/2020-model-software.zip"), "Error! zip_uri does not match!"

### Regular expression for RxHCC sub-zipfile
### Some flexibility built into the pattern with \d and \w
RxHCC_PAT = r"\bRxHCC\b\s+?\bsoftware\b\s+?\w+?\d+?\.\d+?\.\w\d\.zip"

### The sample file we'll use is AGESEXV4.TXT. Here's a pattern to help that out.
agesex_pat = r"AGESEXV\d+?\.TXT"

# The coup de grâce is a method to:
#  * Open the top-level zip;
#  * Match our zipfile name patter (RxHCC...);
#  * Read that file into a bytes buffer;
#  * Match our targeted filename pattern (AGESEXV4.TXT); and
#  * Open the file, read, and decode it into a variable.
def get_file_content(*args):
    with ureq.urlopen(uc.zip_uri) as resp:
        zf = zipfile.ZipFile(BytesIO(resp.read()))
        for fn in zf.namelist():
            if re.match(args[0], fn):
                with zf.open(fn) as zf2:
                    zf2_data = BytesIO(zf2.read())
                    with zipfile.ZipFile(zf2_data) as zfn:
                         for f in zfn.namelist():
                             if re.match(args[1], f):
                                 with zfn.open(f) as zff:
                                     data_ = zff.read().decode("utf-8")

    zf.close()
    return data_

### Run our function with a few regex arguments.
raw_data = get_file_content(RxHCC_PAT, agesex_pat)



### This is being run via Linux,
### so we'll update the line separators and print the file contents, which should be an SAS metho
data = raw_data.replace("\r\n", linesep)
print(data)
