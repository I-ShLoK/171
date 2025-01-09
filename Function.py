#!/usr/bin/env python
# coding: utf-8

# In[4]:


def mean_value(*n):
    sum = 0 
    counter = 0
    for x in n:
        counter = counter +1
        sum +=x
    mean = sum/counter
    return mean


# In[6]:


mean_value(4,10,5,6)


# In[8]:


def product(*n):
    result = 1
    for i in range(len(n)):
        result *= n[i]
    return result


# In[10]:


product(5,1,2,3,6,8)


# In[ ]:




