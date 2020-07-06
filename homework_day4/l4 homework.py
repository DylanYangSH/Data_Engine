#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas 
import numpy as np
from efficient_apriori import apriori


# In[36]:


#header=None, 
db=pandas.read_csv('D:\data analayse\python\lesson 4 home work\Market_Basket_Optimisation.csv',header=None)
print(db.shape)


# In[38]:


tr=[]
for i in range(0, db.shape[0]):
    temp=[]
    for j in range (0,20):
        if str(db.values[i, j]) != 'nan':
            temp.append(str(db.values[i, j]))
    tr.append(temp)
print(tr)


# In[32]:


itemsets,rules = apriori(tr,min_support=0.02, min_confidence=0.4)


# In[33]:


print("频繁项集：", itemsets)
print("关联规则：", rules)


# In[ ]:





# In[ ]:




