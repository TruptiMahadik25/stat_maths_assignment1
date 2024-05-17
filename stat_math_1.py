#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Que no 1

A = set(['a','b','c'])

S = {1,2,3}

def cartesian_product(S1,S2):
    result = set()
    for i in S1:
        for j in S2:
            result.add(tuple([i,j]))
    return (result)

C = cartesian_product(A,S)
print("Cartesian product of A and S\n{} X {}:{}".format(A,S,C))


# In[ ]:





# In[2]:


# #Que no 2

import itertools

A = {'Red','Green','Blue'}
permute_all = set(itertools.permutations(A))
print("Permutations of {}".format(A))
print("-"*50)
for i in permute_all:
    print(i)
print("-"*50)
print ("Number of permutations: ", len(permute_all))



# In[ ]:





# In[3]:


# #Que no 3

n = 1018
pnull = .52
phat = .56

import statsmodels.api as sm

sm.stats.proportions_ztest(phat * n, n, pnull, alternative='larger')


# In[ ]:





# In[4]:


# #Que no 4

S1 = set([x for x in range(31) if x%3==0])
print ("Set S1:", S1)

S2 = set([x for x in range(31) if x%5==0])
print ("Set S2:", S2)

S_difference = S2-S1
print("Difference of S1 and S2 i.e. S2\S1:", S_difference)

S_difference = S1.difference(S2)
print("Difference of S2 and S1 i.e. S1\S2:", S_difference)



# In[ ]:





# In[11]:


# #Que no 5.1

def random_array(num_elements,lower=1,upper=100):
    """
    """
    from random import randint
    lst = []
    for _ in range(num_elements):
        lst.append(randint(lower,upper))
    return lst


# In[16]:


print(arr)


# In[17]:





# In[ ]:





# In[12]:


# #Que no 5.2

def std_dev(array):
    """
    Computes std. deviation
    """
    from math import sqrt
    return (sqrt(variance(array)))


# In[13]:


std_dev(arr)


# In[ ]:





# In[14]:


# #Que no 5.3

def mean(array):
    """
    Computes mean
    """
    length = len(array)
    sum = 0
    for i in range(length):
        sum+=array[i]
    mean = sum/length
    return mean


# In[15]:


mean(arr)


# In[ ]:





# In[18]:


# #Que no 5.4

def variance(array):
    """
    Computes variance
    """
    length = len(array)
    avg = mean(array)
    sumsq = 0
    for i in range(length):
        sumsq+=(array[i]-avg)**2
    variance = sumsq/length
    return variance


# In[19]:


variance(arr)


# In[ ]:




