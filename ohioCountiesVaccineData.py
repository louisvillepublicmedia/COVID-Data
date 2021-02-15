#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
pop_df = pd.read_csv('/Users/suhailbhat/Desktop/COVID-Data/oh-county-vaccine-data/ohio-counties-pop-2019.csv')
vaccine_data = pd.read_csv('/Users/suhailbhat/Desktop/COVID-Data/vaccine_data.csv')

vaccine_data = vaccine_data.groupby('county').sum().reset_index()
vaccine_data['county'] = vaccine_data.county.str.strip()

merged_data = pd.merge(vaccine_data, pop_df, left_on='county', right_on='county_name')

merged_data['pct_pop_firstdose'] = (merged_data[
    'vaccines_started'] * 100 / merged_data['pop_2019']).round(2)
merged_data['pct_pop_vaccinated'] = (merged_data[
    'vaccines_completed'] * 100 / merged_data['pop_2019']).round(2)

merged_data=merged_data[['county_fips',
       'county_name', 'state', 'pop_2019', 'vaccines_started', 
        'vaccines_completed', 'pct_pop_firstdose',
       'pct_pop_vaccinated']]

merged_data.to_csv("/Users/suhailbhat/Desktop/COVID-Data/oh-county-vaccine-data/oh-counties-vaccine-data.csv", index=False)







