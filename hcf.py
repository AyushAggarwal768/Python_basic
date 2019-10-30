#!/usr/bin/env python
# coding: utf-8

# In[1]:


def b(x,y):
    if(x>y):
        k=x
    else:
        k=y
    while(k>0):
        if(x%k==0)&(y%k==0):
            return("hcf is",k)
            break
        k=k-1     


# In[2]:


b(3,4)


# In[ ]:




