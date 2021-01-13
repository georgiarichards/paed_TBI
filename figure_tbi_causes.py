#!/usr/bin/env python
# coding: utf-8

# # Figures for our systematic reivew on traumatic brain injury related paediatric mortality and morbidity in low- and middle-income countries

# #### The protocol and details on our study is available [here](https://www.crd.york.ac.uk/prospero/display_record.php?RecordID=171276). 

# In[1]:


# import libraries required for analysis 
import numpy as np 
import pandas as pd
from pylab import savefig
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# import data 
df = pd.read_csv("causes_TBI.csv",thousands=',')


# In[3]:


df.head()


# In[8]:


# plotting the causes of pTBI 
plt.figure(figsize=(15,10))
ax = sns.barplot(data=df, x="causes_TBI", y="N", color="navy")
plt.xlabel(' ')
plt.ylabel('Number of cases', fontsize=15)

plt.savefig("fig_causes.png", dpi=600)


# In[ ]:




