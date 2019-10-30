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


# In[3]:


def c(x):
    k=0
    b=1
    while(b<(x+1)):
        if(x%b==0):
            k=k+1
        b=b+1
    if(k==2):
        return(x,"is prime")
    else:
        return(x,"is not prime")


# In[5]:


c(8)


# In[ ]:




