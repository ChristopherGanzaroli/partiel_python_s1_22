#!/usr/bin/env python
# coding: utf-8

# In[21]:


def fibonacci(n):
    l = []
    a =0
    b =1
    print('La suite fibonacci est : ')
    while a < n : # tant que a est inférieur au nombre saisie
        l.append(a) # imprime a
        a, b = b, a+b # a égale b et b égale b+a.

    return l


# In[20]:


fibonacci(54)


# In[ ]:




