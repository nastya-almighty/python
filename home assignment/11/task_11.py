#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
from sympy import *
from sympy.plotting import plot
init_printing()


# In[4]:


x = Symbol('x')


# In[6]:


f = x**3 - 50*x
f


# In[8]:


g = -x**4 + 88*x**2 - 241
g


# In[10]:


plot(f, g)


# In[12]:


common = f - g
plot(common)


# In[15]:


result = solve(common)
result


# In[22]:


w = lambda i: i.evalf(5, chop = True)
list(map(w, result))

