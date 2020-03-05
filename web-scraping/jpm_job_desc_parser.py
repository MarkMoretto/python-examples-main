"""
Purpose: Parse JPMorgan job description.
Date created: 2020-03-04

Contributor(s):
    Mark Moretto
"""

import re
import textwrap as tw
import urllib.request as ureq
from platform import python_version_tuple as pvt


### JPMorgan job id
job_id = "285143" # Enter job id here


### Select distinctive keyword to help find actual job description in the raw data.
keyword = "Alteryx" # Enter job keyword here




class VersionException(Exception):
    pass


class IncorrentVersion(VersionException):
    """Exception raised for Python version requirement errors.

    Attributes:
        message - explanation of the error
    """

    def __init__(self, message):
        self.message = message



### This script uses f-strings, which was implemented in Python 3.6.x.
### Ref: https://www.python.org/dev/peps/pep-0498/
min_reqd_ver = 36
if int("".join(pvt()[:2])) < min_reqd_ver:
    raise IncorrentVersion("Please upgrade Python to version 3.6 or better.")

def key_check(iterable):
    """Check and return single list result."""
    if len(iterable) != 1:
        raise ValueError("Multiple description keys found!")
    else:
        return iterable[0]


if __name__ == "__main__":

    url = f"https://jobs.jpmorganchase.com/ShowJob/Id/{job_id}"
    
    ### Read and decode raw data.
    with ureq.urlopen(url) as resp:
        raw_data = resp.read().decode("utf-8")
    
    ### "Tokenize" and create a dictionary for all non-blank lines
    html_tokens = [i.strip() for i in raw_data.split("\n") if len(i) > 0]
    tdict = {k:v for k, v in enumerate(html_tokens)}
    
    
    ### Retrieve all line numbers where the keyword is found.
    desc_key = [k for k, v in tdict.items() if keyword in v]
    title_key = [k for k, v in tdict.items() if "<title>" in v]
    
    
    ### Check for a result of 1; Raise error if any other number returned.
    desc_key = key_check(desc_key)
    title_key = key_check(title_key)
    
    
    ### Clean and process job description section.
    raw_desc = tdict.get(desc_key)
    raw_desc = re.sub("&amp;", "&", raw_desc)# Replace ampersand code.
    raw_desc = re.sub("&nbsp;", "", raw_desc) # Replace non-breaking space
    raw_desc = re.sub("<br>", "", raw_desc) # Replace line breaks
    raw_desc = re.sub(r"<div", "\n<div", raw_desc) # Add line break between <div> tags
    raw_desc = re.sub(r"<\/div>?", "</div>\n", raw_desc) # Add line break between <div> tags
    raw_desc = raw_desc.strip()
    
    #### Use regular expressions to split up some div tags for chunking by section.
    div_pat = r"\n?<div>(.*)?<\/div>\n?(?:<ul><li>)?(.*)?(?:<\/li><\/ul>)?"
    p = re.compile(div_pat)
    res = p.findall(raw_desc)
    
    
    ### Split, process, and format title section for output.
    raw_title = tdict.get(title_key)
    title = re.sub(r"(<\/?title>)", "", raw_title)
    title = re.sub("&amp;", "&", title)
    title_tokens = re.split(r"\s+?-\s+?", title)
    
    job_title = " ".join(title_tokens[:4])
    job_title = "Job title:\n" + "\n".join(
            tw.wrap(job_title, width=90,
                    initial_indent="        ",
                    subsequent_indent="        ")
            )
    
    job_loc, jpm_name = re.split(r"\s+?\|\s+?", title_tokens[4])
    job_loc = f"Location:\n\t{job_loc}, USA"
    
    output_title = f"\n{jpm_name}\n\n{job_title}\n\n{job_loc}\n\n"
    # print(output_title)
    
    
    ### Append formatted results to general list;
    ### We're aiming for a column width of ~95 characters
    ### List items should be formatted accordingly.
    output_desc = list()
    nl_frmt = "   * "
    for i in res:
        if len(i[0]) > 0:
            output_desc.append("\n".join(tw.wrap(i[0], width=95)))
        if len(i[1]) > 0:
            tmp = re.sub(r"(<\/li><li>)", "`", i[1])
            tmp = re.split(r"<\/li><\/ul>", tmp)[0]
            lst = tmp.split("`")
            chunks = \
                [tw.fill(i, width=90, initial_indent = nl_frmt, subsequent_indent="     ")
                for i in lst]
            output_desc.append("\n".join(chunks))
    
    ### Print results to terminal
    print(output_title + "\n\n".join(output_desc))
