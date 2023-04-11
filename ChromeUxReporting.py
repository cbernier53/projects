#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[77]:


df = pd.read_csv('chromeux.csv')
fcp = df.groupby(['origin', 'device', 'start'])[['density']].agg('sum')
fcp.to_csv('fcp.start.csv')
fcp


# In[78]:


lcp = pd.read_csv('chromeux1.csv')
lcp = lcp.groupby(['origin', 'lcpe'])[['lcpd']].agg('sum')
lcp.to_csv('lcp.csv')
lcp


opl = pd.read_csv('opl.csv')
opl = opl.groupby(['origin','onend'])[['density']].agg('sum')
opl.to_csv('ocp.csv')
opl



fid = pd.read_csv('fid1.csv')
fid = fid.groupby(['origin','fidend'])[['density']].agg('sum')
fid.to_csv('fid.csv')
fid



# In[ ]:




