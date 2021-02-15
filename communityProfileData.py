#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import re
import requests
import numpy as np
from bs4 import BeautifulSoup
from glob import iglob

state_df = pd.read_excel(open(next(iglob('Community_Profile_Report*.xlsx')),'rb'), sheet_name='States')

# make first row as header
state_df.columns = state_df.iloc[0]
state_df = state_df[1:]
state_df.to_csv("cdcCovidDataByState.csv", index=False)

df = pd.read_excel(open(next(iglob('Community_Profile_Report*.xlsx')),'rb'), sheet_name='Counties')

# make first row as header
df.columns = df.iloc[0]
df = df[1:]

# drop unallocated columns
df=df.drop(df[df.County.str.contains("Unallocated")].index)

# add zero to 4-digit fips and convert to string for GeoJson join
df["FIPS code"] = df["FIPS code"].astype(str).str.zfill(5)

df=df.rename(columns={"FIPS code" : "county_fips"})

df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('SustainedHotspot', 'Sustained Hotspot')
df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('Hotspot', 'Hotspot')
df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('HighBurdenResolving', 'High Burden Resolving')
df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('ModerateBurdenResolving', 'Moderate Burden Resolving')
df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('EmergingHotspot', 'Emerging Hotspot')
df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('ModerateBurden', 'Moderate Burden')
df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('LowBurden', 'Low Burden')

#save the file to be uploaded to github
df.to_csv("latest-cdc-covid-data-by-county.csv", index=False)


# In[ ]:




