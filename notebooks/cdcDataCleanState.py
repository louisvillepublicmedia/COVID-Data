#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
import requests
import numpy as np
from bs4 import BeautifulSoup
from glob import iglob

df = pd.read_excel(open(next(iglob('Community_Profile_Report*.xlsx')),'rb'), sheet_name='States')

# make first row as header
df.columns = df.iloc[0]
df = df[1:]

df.to_csv("cdcCovidDataByState.csv", index=False)


# In[ ]:




