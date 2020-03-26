"""
Purpose: Get coronavirus data from various sources
Date created: 2020-03-26

Contributor(s):
    Mark M.

Project folder: C:\\\\covid-19\web-scraping
"""

import os
import json
import pandas as pd
import urllib.request as ureq
from datetime import datetime as dt


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expcond

# Change local folder to current directory
project_folder = r"C:\path\to\folder\covid-19\web-scraping"
os.chdir(project_folder)

# Path to chromedriver
driver_pth = f"{project_folder}\chromedriver.exe"
chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application"

os.environ["PATH"] = os.environ["PATH"] + f";{chrome_path}"


site = "nyt"
csv_name = "CasesByState"
csv_path = f"src\csv-files\{csv_name}.csv"


def process_df(dataframe):
    col_dict = {k:v.lower() for k, v in enumerate(dataframe.loc[0].values)}
    dataframe = dataframe.rename(columns=col_dict)
    dataframe.drop(0, inplace=True)
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


def scrape_nyt():
    nyt_url = "https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html"
    data_list = list()
    with webdriver.Chrome() as chdriver:
        chdriver.get(nyt_url)

        btn_show_more = WebDriverWait(chdriver, 10) \
                            .until(expcond.presence_of_element_located((By.CSS_SELECTOR,"#g-cases-by-state button[class^='svelte']")))
    
        chdriver.execute_script("arguments[0].click()", btn_show_more)
        for element in WebDriverWait(chdriver, 10).until(expcond.presence_of_all_elements_located((By.CSS_SELECTOR,"#g-cases-by-state table[class^='svelte'] tr"))):
            tbl_data = [i.text for i in element.find_elements_by_css_selector("th,td")]
            data_list.append(tbl_data)

    if len(data_list) > 0:
        df1 = process_df(data_list)
        return process_df(df1)


df = scrape_nyt()
df["date_retrieved"] = pd.to_datetime(dt.now()).strftime("%Y-%m-%d")
df["source"] = site


# Append to csv document
with open(csv_path, mode="a", encoding="utf-8", newline="\n") as f:
    df.to_csv(f, index=False, header=f.tell()==0, line_terminator="\n", encoding="utf-8")





#################################################################################
### CDC US daily - Cumulative

site = "cdc_gov"
csv_name = "DailyAccumulatedCases"
csv_path = f"src\csv-files\{csv_name}.csv"

cdc_json_url = "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/total-cases-onset.json"
with ureq.urlopen(cdc_json_url) as resp:
    data = resp.read().decode("utf-8")

json_data =  json.loads(data)
core_data = json_data.get("data").get("columns")
dates = core_data[0][1:]
start_of_tracking = [f"{i}" for i in range(1, len(dates) - 9)]
values = core_data[1][1:]
df_data = list(zip(dates, start_of_tracking, values))
df_columns = ["Reported Date", "Start of Tracking", "Total number of accumulated cases",]

df = pd.DataFrame(data=df_data, columns=df_columns)

df.to_csv(csv_path, index=False)



#################################################################################
### CDC US daily - onset

site = "cdc_gov"
csv_name = "DailyReportedCasesUS"
csv_path = f"src\csv-files\{csv_name}.csv"


cdc_json_url = "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/us-cases-epi-chart.json"
with ureq.urlopen(cdc_json_url) as resp:
    data = resp.read().decode("utf-8")

json_data =  json.loads(data)
core_data = json_data.get("data").get("columns")
dates = core_data[0][1:]
start_of_day = [f"{i}" for i in range(len(dates) - 10)]
start_of_day += ["Not all illnesses reported" for _ in range(10)]
values = core_data[1][1:]
df_data = list(zip(dates, start_of_day, values))
df_columns = ["Reported Date", "Start of Day", "Number of cases",]

df = pd.DataFrame(data=df_data, columns=df_columns)

df.to_csv(csv_path, index=False)





#################################################################################
### Michigan - Cases by County

site = "mich_gov"
csv_name = "CasesByCounty"
csv_path = f"src\csv-files\{csv_name}.csv"

mich_url = "https://www.michigan.gov/coronavirus/0,9753,7-406-98163-520743--,00.html"

res = pd.read_html(mich_url)
dfm = res[0]
df = process_df(dfm)
df["date_retrieved"] = pd.to_datetime(dt.now()).strftime("%Y-%m-%d")
df["source"] = site

with open(csv_path, mode="a", encoding="utf-8", newline="\n") as f:
    df.to_csv(f, index=False, header=f.tell()==0, line_terminator="\n", encoding="utf-8")






# GitHub data
# FIPS and Admin2: https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697

section = "JohnsHopkinsCovidData"
csv_name = f"src\csv-files\{section}.csv"
xl_name = f"src\csv-files\{section}.xlsx"

gh_index_url = "https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports"
res = pd.read_html(gh_index_url)
df1 = res[0]
dates = df1.loc[df1["Name"].str.endswith("csv"), :]["Name"].values.tolist()
dates = dates[::-1]


col_dict = {
 'Province/State':'Province_State',
 'Country/Region':'Country_Region',
 'Last Update':'Last_Update',
 'Latitude':'Lat',
 'Longitude':"Long_"
 }


dfs = pd.DataFrame(columns=['FIPS','Admin2','Province_State','Country_Region','Last_Update','Lat','Long_','Active','Combined_Key'])

for d in dates:
    tmp_url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{d}"
    dfx = pd.read_csv(tmp_url)
    dfx = dfx.rename(columns=col_dict)
    dfs = dfs.append(dfx, sort=False)


df = dfs.drop(['FIPS','Lat', 'Long_','Combined_Key',], axis=1).copy()
df = df.reset_index(drop=True)
df.loc[:, "Last_Update"] = pd.to_datetime(df.loc[:, "Last_Update"], infer_datetime_format=True)
df.loc[:, "Last_Update"] = df.loc[:, "Last_Update"].dt.strftime("%Y-%m-%d")

df.to_csv(csv_name, index=False, float_format="%.0f")

df.to_excel(xl_name, index=False, float_format="%.0f")

