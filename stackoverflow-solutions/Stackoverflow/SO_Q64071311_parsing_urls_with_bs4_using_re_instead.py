
"""
Purpose: Stackoverflow question.
Title: Having trouble extracting img src from multiple URLs with beautifulsoup4 on Python3
Date created: 2020-09-25
URL: https://stackoverflow.com/questions/64071311/having-trouble-extracting-img-src-from-multiple-urls-with-beautifulsoup4-on-pyth/64072115#64072115
Contributor(s):
    Mark M.
"""

import re


html = """
<ul class="bxslider" style="width: 1315%; position: relative; left: -410px;">
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;" class="bx-clone"><img src="//d1w0x2adoh4nzy.cloudfront.net/b5/48/b548ce05-1ee1-486b-9f33-ea61625d25ba.jpg"></li>
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;"><img src="//d1w0x2adoh4nzy.cloudfront.net/50/1f/501f8112-f6a7-4710-bd48-3acb0976e8f3.jpg?timestamp=1600972726783"></li>
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;"><img src="//d1w0x2adoh4nzy.cloudfront.net/55/bb/55bb9511-676b-4585-8cf2-99af9ba8baca.jpg"></li>
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;"><img src="//d1w0x2adoh4nzy.cloudfront.net/06/a7/06a700dd-8350-4932-88e9-c941e73e0def.jpg"></li>
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;"><img src="//d1w0x2adoh4nzy.cloudfront.net/8c/92/8c92207d-c422-4d94-894c-911a5330e227.jpg"></li>
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;"><img src="//d1w0x2adoh4nzy.cloudfront.net/e0/22/e0224832-75f5-432a-a223-177ff7ffd03c.jpg"></li>
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;"><img src="//d1w0x2adoh4nzy.cloudfront.net/8a/e1/8ae1e8d4-76a1-4161-9b17-b7a97e1779fc.jpg"></li>
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;"><img src="//d1w0x2adoh4nzy.cloudfront.net/fc/d5/fcd5a35b-8fb5-463e-9a47-804850f17825.jpg"></li>
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;"><img src="//d1w0x2adoh4nzy.cloudfront.net/98/2e/982ea3c5-ce28-49c8-bef5-b0f85bd99807.jpg"></li>
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;"><img src="//d1w0x2adoh4nzy.cloudfront.net/23/e1/23e153df-75af-4f1b-a4dd-3e0fb1e5a28f.jpg"></li>
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;"><img src="//d1w0x2adoh4nzy.cloudfront.net/94/02/940268f9-04ed-4650-bd9f-01b113b5059b.jpg"></li>
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;"><img src="//d1w0x2adoh4nzy.cloudfront.net/b5/48/b548ce05-1ee1-486b-9f33-ea61625d25ba.jpg"></li>
    <li style="float: left; list-style: outside none none; position: relative; width: 410px;" class="bx-clone"><img src="//d1w0x2adoh4nzy.cloudfront.net/50/1f/501f8112-f6a7-4710-bd48-3acb0976e8f3.jpg?timestamp=1600972726783"></li>
</ul>
"""
# Retrieve only list elements based on given <ul> class
list_section_pattern = r'(?:<ul class="bxslider" .*?>)(?P<target>.*?)(?:</ul>)'
p = re.compile(list_section_pattern, flags = re.DOTALL | re.MULTILINE)
list_section = p.search(html).group("target")



# Match pattern to get all URLs; This is pretty straightforward.
href_pattern = r'<img src="(.*?)">'
p = re.compile(href_pattern)
urls = p.findall(list_section)

def get_root_url(url_path):
    """Split by forward-slash; Keep everything except image filename."""
    return "/".join(url_path.split(r"/")[:-1])


# Create a dictionary of url roots and image url lists.
url_dict = {}
for url in urls:
    root = get_root_url(url)
    if not root in url_dict:
        url_dict[root] = [url]
    else:
        url_dict[root].append(url)

# Output string for csv file
csv_string = ""
for k, v in url_dict.items():
    # Join() elements with vertical bar.
    tmp = " | ".join(v)
    csv_string += f"{k}, {tmp}\n" # Add a newline character

with open(r"C:\Users\Work1\Desktop\GitHub\didthisworklol.csv", "w", encoding="utf-8") as csvf:
    csvf.write(csv_string)



#####################################################
from bs4 import BeautifulSoup as bs

soup = bs(html, "html.parser")

# res = soup.find_all("ul", class_="bxslider")
# # table = soup.find('ul', attrs={'class':'bxslider'})

# img_res = res[0].find_all("img")
# for img in img_res:
#     url = img.attrs["src"]
#     print(url)

# This should return all unordered list sections with the class 'bxslider'
for chunk in soup.find_all("ul", class_="bxslider"):
    # List comprehension to get all the urls from the img tag.
    urls = [img.attrs["src"] for img in chunk.find_all("img")]

    url_dict = {}
    for img in chunk.find_all("img"):
        url_ = img.attrs["src"]
        root_ = get_root_url(url_)
        if not root_ in url_dict:
            url_dict[root_] = [url_]
        else:
            url_dict[root_].append(url_)










