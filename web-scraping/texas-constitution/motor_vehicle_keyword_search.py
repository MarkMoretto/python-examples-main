"""
Purpose: Process and find keywords in Texas Constitution
Date created: 2020-11-01

Contributor(s):
    Mark Moretto
"""

import os
import re
import requests

"""
Keywords to find within Texas constitution documents.
"""
keywords = ("noise", "sound", "nuisance")


"""
Summary -
    Since we know the "groups" of pages to search, we can limit data by skipping irrelevant
    sections (motorcycle, commerical vehicle, non motor vehicle).

Variables - 
    :general_start: Start of motor vehicle section based on query_url (below)
    :skip_start: segment with motorcycles, commercial vehicles.
    :skip_end: end of segment with motorcycles, commercial vehicles.
"""
index_kwargs = dict(general_start = 501, skip_start = 621, skip_end = 680)

"""
    :base_url: Core URL we'll be using
    :query_url: Query segment to get data from the correct section.
    :base_link_url: The URL base segment for related subpages.
"""
base_url = "https://statutes.capitol.texas.gov"
query_url = f"{base_url}?link=TN"
base_link_url = rf"{base_url}/Docs/TN/htm/" # (i.e. - https://statutes.capitol.texas.gov/Docs/TN/htm/TN.1.htm)


def get_and_clean_data(url):
    """Function to get data from a given URL, then remove any newline
    tab, and multiple space characters.  Those will be replaced with
    single whitespace chracters.
    
    Params -
        :url: Core URL from which to retrieve and clean data    
    """
    
    resp = requests.get(url)
    d = ""
    if resp.status_code == 200:
        d = resp.text
        d = re.sub(r"([\n|\s|\t]+)", "  ", d)
        d = re.sub(r"(\s){2,}", " ", d)
    return d.strip()


def create_links_dictionary(url, **index_kwargs):
    """Process data and return collection of webpage links."""
    
    data = get_and_clean_data(query_url)
    p = re.compile(rf'\shref\={re.escape(base_link_url)}([\w\d\.]+)\s?', flags = re.I)
    tmplinks = p.findall(data)


    # Create key-value pair data collection
    links_dict = dict(map(lambda x: (f"{base_link_url}{x}",
                                     re.sub(r"TN\.([\d\w]+)\..*", r"\1", x)), tmplinks))


    # Get index key-value pairs
    general_start = index_kwargs.get("general_start")
    skip_start = index_kwargs.get("skip_start")
    skip_end = index_kwargs.get("skip_end")
    
    # Reduce link count
    target_links = []
    for i, v in links_dict.items():
        # Only keep numerical values from key since some end with a letter.
        ii = int(re.sub(r"\D+", '', i))
        if ii >= general_start and (ii > skip_end or ii < skip_start):
            target_links.append(i)
            
    


# Find and return sections of texas constitution based on
# matching keyword results, which we defined above
# Pre-process keywords and add to results collection

results = []
kwrd_pattern = "("+"|".join(keywords)+")"
p = re.compile(kwrd_pattern, flags = re.I)

for link in target_links:
    data = requests.get(link).text
    if not data is None:
        # Clean up HTML data (remove tags, add newline char)
        dlist = re.split(r"\n",
                         re.sub(r"\s{2,}", "\n",
                                re.sub(r"<.*?>", "  ", data).strip()
                                )
                         )
        for i, line in enumerate(dlist):
            if p.search(line):
                l = link.split("/")[-1]
                # results.append(f"{l}\t{i}\t{tw.fill(line)}")
                line = re.sub(r"([\t|\n])", " ", line)
                results.append(f'{l}\t{i}\t{line}')




if len(results) > 0:
    output = "PAGE\tLINE NO\tSNIPPET\n"
    output += "\n".join(results)
# print(msg)

# Write results to csv file.
user = os.environ["UserName"]
DOCUMENTS_DIR = rf"C:\Users\{user}\Documents"
with open(rf"{DOCUMENTS_DIR}\tex-statutes-matches.txt", "w") as outf:
    outf.write(output)
