#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
x = np.array(["A",67,57,9,8])
print(x)
print(type(x))
print(x.dtype)


# In[15]:


a2 = np.array([[20,40],[30,60]])
print(a2)
print(type(a2))
print(a2.shape)
print(a2.dtype)


# In[17]:


a = np.array([10,20,30,40])
b = a.reshape(2,2)
print(b)
print(b.shape)


# In[ ]:


#USE OF AROUND()
d = np.array([1.23565'


# In[19]:


a2 = np.array([[3,4,6],[7,9,10],[4,6,12]])
a2


# In[21]:


print(a2.sum(axis=1))
print(a2.sum(axis=0))


# In[25]:


np.mean(a2.sum(axis=1))


# In[ ]:


A = np.array([[1,2],[2,5]

