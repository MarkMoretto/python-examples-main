
"""
Purpose: CFPB Analysis
Date created: 2020-06-16

Contributor(s):
    Mark M.
"""

import requests
import pandas as pd


hmda_base = "https://api.consumerfinance.gov"
complaints_base = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/1"
complaints_states_base = f"{complaints_base}/geo/states"




hmda_concepts_url = f"{hmda_base}/data/hmda/slice/hmda_lar/metadata.json"


with requests.Session() as s:
    resp = s.get(hmda_concepts_url)
    if resp.status_code == 200:
        # If status okay, read data into variable
        json_data = resp.json()

fields = json_data.get("dimensions")


def query_to_df(query: str):
    outdf = pd.DataFrame
    dd = None
    with requests.Session() as s:
        resp = s.get(query)
        if resp.status_code == 200:
            # If status okay, read data into variable
            json_data = resp.json()
    
            # Get table and data subset from response json
            dd = json_data.get("table").get("data")

    if not dd is None:
        # Create pandas dataframe from results
        return outdf(dd)

# Example to get all agency names and abbreviations.
agency_all_url = f"{hmda_base}:443/data/hmda/concept/agency_code.json"
data = query_to_df(agency_all_url)


qry_params = {
        '$select': 'agency_code, agency_name, applicant_ethnicity, applicant_ethnicity_name, applicant_income_000s',
        '$limit': '10',
        '$offset': '0',
        '$format': 'json',
        }











