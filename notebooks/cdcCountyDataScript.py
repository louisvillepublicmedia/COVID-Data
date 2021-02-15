#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import re
import requests
import numpy as np
from bs4 import BeautifulSoup
from glob import iglob


# xls = pd.ExcelFile('Community_Profile.xlsx')

# # # Now you can list all sheets in the file
# xls.sheet_names
# # # to read just one sheet to dataframe:
# df = pd.read_excel("Community_Profile.xlsx", sheet_name="Counties")
# df = pd.read_excel(open('Community_Profile.xlsx','rb'), sheet_name='Counties')
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


# ## promote the GEOID property in our GeoJSON file
# 
# // before
# { 
# 'type': 'Feature', 
# 'properties': { 
#   'GEOID': '01005', // promote this property as an id
#   ...
#   },
#   ...
# }
# 
# // after
# { 
# 'type': 'Feature', 
# 'id': 1005, // id from GEOID
# 'properties': {
#   'GEOID': '01005', 
#   ...
#   },
#   ...
# }

# In[7]:


# import json

# with open('us-counties-filter.geojson') as f:
#   data = json.load(f)
#   for item in data['features']:
#     item['id'] = item['properties']['GEOID']

#   with open('us-counties-filter-with-id.geojson', 'w') as f:
#     json.dump(data, f)


# In[17]:


# df.head()


# In[4]:


# 'SustainedHotspot' : 'Sustained Hotspot' 
# Hotspot : Hotspot
# HighBurdenResolving : HighBurdenResolving
# ModerateBurdenResolving : ModerateBurdenResolving
# EmergingHotspot : EmergingHotspot
# ModerateBurden : ModerateBurden
# lowburden : lowburden


# In[13]:


# df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('SustainedHotspot', 'Sustained Hotspot')
# df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('Hotspot', 'Hotspot')
# df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('HighBurdenResolving', 'High Burden Resolving')
# df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('ModerateBurdenResolving', 'Moderate Burden Resolving')
# df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('EmergingHotspot', 'Emerging Hotspot')
# df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('ModerateBurden', 'Moderate Burden')
# df['Area of Concern Category'] = df['Area of Concern Category'].str.replace('Lowburden', 'Low Burden')


# In[14]:


# df['Area of Concern Category'].value_counts()


# In[ ]:




