"""
Script to read and parse CMS.gov hcc risk-adjusted software files
URI: https://www.cms.gov/Medicare/Health-Plans/MedicareAdvtgSpecRateStats/Risk-Adjustors

Notes:
	* No local files or folders are created
		--> Imported data remains in memory buffer
	* Shows handling of compressed files that are nested
	* Demonstrates part of cleaning process to make useable data
"""

import re
import zipfile
from io import StringIO, BytesIO
import urllib.request as ureq
import pandas as pd

model_year = '2020'
cms_hcc_uri = f"https://www.cms.gov/files/zip/{model_year}-model-software.zip"


# raw_data = BytesIO(ureq.urlopen(cms_hcc_uri).read())
# raw_data.seek(0)

zf_buffer = BytesIO(ureq.urlopen(cms_hcc_uri).read())

def print_namelist(zipfile_buffer):
    with zipfile.ZipFile(zipfile_buffer) as zf:
        print(zf.namelist())



#-- Read nested zipfile
zipfile_kwrd = 'RxHCC'
filename_kwrd = 'scorevar'
with zipfile.ZipFile(zf_buffer) as zf:
    for f in zf.namelist():
        if zipfile_kwrd in f:
            with zf.open(f) as subz:
                zip_data = BytesIO(subz.read())
                if zipfile.is_zipfile(zip_data):
                    with zipfile.ZipFile(zip_data) as zf2:
                        for f in zf2.namelist():
                            if filename_kwrd in f.lower():
                                with zf2.open(f) as targetf:
                                    raw_data = targetf.read().decode('utf-8')


zf_buffer.close()

#-- Get ICD mappings
#-- May require more general uri search if looking for non-midyear files
cms_icd_mappings_uri = f"https://www.cms.gov/Medicare/Health-Plans/MedicareAdvtgSpecRateStats/Downloads/{model_year}MidyearFinalICD-10-CMMappings.zip"

zf_buffer = BytesIO(ureq.urlopen(cms_icd_mappings_uri).read())
# print_namelist(zf_buffer)


file_extension = ('csv')
with zipfile.ZipFile(zf_buffer) as zf:
    for f in zf.namelist():
        if f.endswith(file_extension):
            with zf.open(f) as targetf:
                # file_data = targetf.read()
                bbuff = BytesIO(targetf.read())


#-- Read into dataframe from buffer
#-- This will consume the buffer, so re-creating the
#-- dataframe will require re-reading the data from zf_buffer
df = pd.read_csv(bbuff, header=3,)

#-- Reformat columns to remove whitespace, tabs, hyphens, etc.
#-- Replace those items with an underscore
col_dict = dict()
for col in df.columns.values.tolist():
    new_col = re.sub(r"[\n\s-]+", "_", col)
    col_dict[col] = new_col
df = df.rename(columns=col_dict).copy()

#-- Drop NA rows only if the enture row is NA; Reset index values.
df = df.dropna(how='all', inplace=False).reset_index(drop=True)

#-- Keep rows up until ending notes
final_row = df.loc[df['Diagnosis_Code'].str.contains('Note'),:].index[0]
df = df.iloc[:final_row,:]

na_cols = df.isna().sum()
na_cols = na_cols[na_cols>0].index.values

float_cols = df.select_dtypes(include=['float','float64']).columns
df.loc[:, float_cols] = df.loc[:, float_cols].astype(str)

#-- Replace 'nan' with None
for col in na_cols:
    df.loc[df[df[col] == 'nan'].index, col] = None

#-- Rescale floating point values to zero.
for col in na_cols:
    df.loc[~df[col].isna(), col] = df.loc[~df[col].isna(), col].str.split('.', expand=True)[0]

