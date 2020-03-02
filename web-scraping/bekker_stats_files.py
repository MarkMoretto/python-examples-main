
"""
Purpose: Get all stats PDFs from Prof. L. Bekker's website
Date created: 2020-03-02

Contributor(s):
    Mark M.
    
Notes:
	Make sure to set OUTPUT_FOLDER before running.
"""

import re
import os.path
from os import chdir
from shutil import copyfileobj
from urllib.request import urlopen
from urllib.parse import unquote_plus

EXTENSION = "pdf"
EXCLUDE = "syllabus"
OUTPUT_FOLDER = r""

def output_folder_check(fileobj):
	"""Validate and provide default if OUTPUT_FOLDER not valid or not set."""
    DEFAULT_FOLDER = rf"C:\Users\{getuser()}\Downloads"
    if len(fileobj) == 0:
        return DEFAULT_FOLDER
    elif not os.path.isdir(fileobj):
        return DEFAULT_FOLDER
    else:
        return fileobj

OUTPUT_FOLDER = output_folder_check(OUTPUT_FOLDER)
chdir(OUTPUT_FOLDER)


core_url = "https://faculty.fiu.edu/~bekkerl"
resources_url = f"{core_url}/Index%202023.htm"

### Read and decode raw HTML data
with urlopen(resources_url) as f:
    raw_data = f.read().decode("utf-8")


# tokens = [i.strip() for i in raw_data.split("\n") if len(i.strip()) > 0]
# tdict = {i:v for i, v in enumerate(tokens)}


### Extract links from raw_data string
href_ptrn = r'<a\s+?href\="([\w\d_\.\[\]%]+){q}">'.format(q = EXTENSION)
p = re.compile(href_ptrn)
pdf_basenames = set(p.findall(raw_data))


### Create list of pdf names and extensions
pdf_names = [f"{i}{EXTENSION}" for i in pdf_basenames if not EXCLUDE in i.lower()]


### Read, write, and rename pdfs
for n in pdf_names:
    download_url = f"{core_url}/{n}"
    output_path = rf"{OUTPUT_FOLDER}\{n}"
    with urlopen(download_url) as pdff:
        with open(output_path, "wb") as outf:
            copyfileobj(pdff, outf)

    # Rename files for readability.
    # If not in same directory as files, then full path
    # needs to be used instead of just the filenames.
    new_name = re.sub(r"[\s_]+", "-", unquote_plus(n))
    os.rename(n, new_name)
