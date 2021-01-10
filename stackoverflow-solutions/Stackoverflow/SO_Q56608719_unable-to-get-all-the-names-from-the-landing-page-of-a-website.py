

"""
Topic: Getting all colleges from a site without hitting a "show more results" button.


Ref: https://stackoverflow.com/questions/56608719/unable-to-get-all-the-names-from-the-landing-page-of-a-website/56610460#56610460
"""

import re
import requests
from bs4 import BeautifulSoup

url = r'https://www.abhe.org/directory'
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')


js_data = soup.find_all('script') # Get script tags
js_data_2 = [i for i in js_data if len(i) > 0] # Remove zero length strings
js_dict = {k:v for k, v  in enumerate(js_data_2)} # Create a dictionary for referencing
data = str(js_dict[10]) # Our target is key 10

# Clean up results
data2 = data.replace('<script>\r\n\t\tw2dc_map_markers_attrs_array.push(new w2dc_map_markers_attrs(\'e5d47824e4fcfb7ab0345a0c7faaa5d2\',','').strip()

# Split on left bracket
test1 = data2.split('[')

# Remove 'eval(' and zero-length strings
test2 = [i for i in test1 if len(i) > 0 and i != 'eval(']

# Use regex to find strings with numbers between double quotation marks
p = re.compile(r'"\d+"')
test3 = [i for i in test2 if p.match(i)]

# List comprenehsion for index value 6 items, which is the college name
# we also can replace double quotation marks.
college_list = [test3[i].split(',')[6].replace('"','') for i in range(len(test3))]
college_list = sorted(college_list)
