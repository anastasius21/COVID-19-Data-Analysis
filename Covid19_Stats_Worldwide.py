#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

df = pd.read_csv('E:/covid_19_data.csv')
df.drop(['WHO Region','Cases - cumulative total per 100000 population','Cases - newly reported in last 7 days','Cases - newly reported in last 7 days per 100000 population','Cases - newly reported in last 24 hours','Deaths - cumulative total per 100000 population','Deaths - newly reported in last 7 days','Deaths - newly reported in last 7 days per 100000 population','Deaths - newly reported in last 24 hours'],axis=1,inplace=True)
df.rename(columns={'Name':'Countries','Cases - cumulative total':'Cases','Deaths - cumulative total':'Deaths'},inplace=True)


total_cases=df['Cases'].sum()
total_deaths=df['Deaths'].sum()

plt.pie([total_cases,total_deaths],labels=['Total Cases','Total Deaths'],colors=['blue','red'],autopct='%1.1f')
plt.title('Worldwide COVID 19 Stats')
plt.show()


# In[ ]:




