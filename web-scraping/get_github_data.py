
"""
Purpose: Scrape data (csv, txt, etc.) links from GitHub
Date created: 2020-02-07

Contributor(s):
    Mark M.
"""

import re
import os.path
import urllib.request as ureq

import pandas as pd

#-- Extension to target
#-- Can create tuple if multiple extensions desired
FILE_EXTENSION = "csv"

#-- Example user and path to subfolder containing data.
username = "cliburn"
data_subfolder = r"biostatistics-review/tree/master/data"

#-- Base URIs and repo path construction.
base = r"https://github.com"
base_raw = r"https://raw.githubusercontent.com"
repo_uri = ureq.urljoin(base, f"{username}/{data_subfolder}")

#-- Import HTML data
with ureq.urlopen(repo_uri) as f:
    data = f.read().decode('utf-8')

#-- Extract href link from <span> tag; Only keep those that match our extension.
matches = re.findall(r'<span\s.*?href\="(.*?)"', data, flags=re.DOTALL)
csv_links = [ureq.urljoin(base_raw, i) for i in matches if str(i).endswith(FILE_EXTENSION)]

l_dict = {}
for link in csv_links:
    blob_free_link = re.sub(r"(.+)(blob/)(.+)", r"\1\3", link)
    basename = os.path.basename(link).split(".")[0]
    l_dict[basename] = blob_free_link

# Eval each link with pandas (or another method) to draw in data
for k, v in l_dict.items():
    exec_str = f"df_{k} = pd.read_csv(r\"{v}\", header=None,)"
    exec(exec_str)

