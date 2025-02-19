#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

df = pd.read_csv('E:/covid_19_data.csv')
df.drop(['WHO Region','Cases - cumulative total per 100000 population','Cases - newly reported in last 7 days','Cases - newly reported in last 7 days per 100000 population','Cases - newly reported in last 24 hours','Deaths - cumulative total per 100000 population','Deaths - newly reported in last 7 days','Deaths - newly reported in last 7 days per 100000 population','Deaths - newly reported in last 24 hours'],axis=1,inplace=True)
df.rename(columns={'Name':'Countries','Cases - cumulative total':'Cases','Deaths - cumulative total':'Deaths'},inplace=True)

Countries = df['Countries'].unique()
for a in range(0,len(Countries)):
    print(a+1,'. ',Countries[a])
    
xyz = input("Enter any name from the list of the given countries: ")

for x in range(0,len(Countries)): 
    if xyz in Countries[x]:
        C = df[df['Countries']==Countries[x]]
        plt.pie([C['Cases'][x],C['Deaths'][x]],labels=['Cases','Deaths'],colors=['blue','red'],autopct='%1.1f')
        plt.title(Countries[x])
        plt.show()
        break
else:
    print('Your input is invalid. Try Again')
    


# In[ ]:




