#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorielle(num):
   if num == 0:
      return 1
   else:
      F = 1
      for k in range(2,num+1):
         F = F * k

      return F


# In[2]:


factorielle(5)


# In[ ]:




