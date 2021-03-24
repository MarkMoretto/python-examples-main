
"""
Purpose: 
Date created: 2021-03-22
https://stackoverflow.com/questions/66756496/extract-the-data-from-csv-file#66756496
Contributor(s):
    Mark M.
"""


import re
import csv
from pathlib import Path

# ddir = Path(r"C:\Users\Work1\Desktop\Info\PythonFiles")
folder = Path(r"C:\path\to\output\folder")
csv_output_path = folder.joinpath("my-csv-file.csv")


sample = """1 Disease1 01000 01001 01002 01003 01004 01005 01006 01010 01011 01012 01013 01014 01015 01016 01080 01081 01082 01083 01084 01085 01086 01090 01091 01092 01093 01094 01095 01096 01100 01101 01102 01103 01104 01105 01106 01110 01111 01112 01113 01114 1370 1371 1372 1373 1374 V1201

2 Disease2 (except in illness) 0031 0202 0223 0362 0380 0381 03810 03811 03812 03819 0382 0383 03840 03841 03842 03843 03844 03849 0388 0389 0545 449 77181 7907 99591 99592

3 Disease3; unspecified site 0200 0208 0209 0218 0219 0228 0229 0230 0231 0232 0233 0238 0239 024 025 0260 0269 0270 0271 0272 0278 0279 0300 0301 0302 0303 0308 0309 0312 0318 0319 03289 0329 0330 0331 0338 0339 0341 0363 03681 04181 04182 04183 04184 04185 04186 04189 0419 390 3929 7953 79531 79539 V090 V091 V092 V093 V094 V0950 V0951 V096 V0970 V0971 V0980 V0981 V0990 V0991 V1204"""


# Create a regular expression to help segment data into keys and values.
ptrn = r"(.+?)\s+?(?=0)(.+)"
p =re.compile(ptrn)

# temp dictionary to store initial values
ddict = {}
for row in sample.split("\n" * 2):
    # If we find a match
    res = p.search(row)
    if res:
        # Assign key and value variables.
        disease, numbers = res.groups()

        # disease_num, _ = re.split(r"\s+", disease.strip(), 1)
        disease_key = re.search(r"(Disease\d+?)",disease.strip()).group()
        # print(disease_num,  ": ", numbers)
        # disease_key = f"Disease{disease_num}"
        ddict[disease_key] = re.sub(r"\s+", ",", numbers.strip())


# The fun part - Dictionary records

# 'Header' values
csv_columns = ddict.keys()

# Probably a better way to evaluate this...
matrix = []
max_count = -1 # Need equal length "columns" to write.
for i, v in enumerate(ddict.values()):
    matrix.append(v.split(","))
    m_len = len(matrix[i])
    if m_len > max_count:
        max_count = m_len

# You'll have t have each column be equal length
for i, row in enumerate(matrix):
    m_len = len(matrix[i])
    if m_len < max_count:
        matrix[i].extend([""] * (max_count - m_len))

output = []
for r in range(max_count):
    row = (matrix[c][r] for c, val in enumerate(matrix))
    output.append(dict(zip(csv_columns, row)))


# Write using csv.DictWriter
# If on Windows, make sure to include newline = ""
with csv_output_path.open(mode="w", newline="") as outf:
    csv_writer = csv.DictWriter(outf, fieldnames = csv_columns)
    csv_writer.writeheader()
    csv_writer.writerows(output)

    for data in output:
        csv_writer.writerow(data)

