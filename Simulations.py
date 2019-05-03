


import random 
import math
import numpy as np
from scipy import special
import scipy as sp
import scipy.stats



def theoreticalG(c, a , n, randomList): #should return the list of papers an author has up to time n/n+1
    beta = c/float(c+a)
    y = []
    for j in range(1,n+1):
        temp = a*(np.power(j/float(n+1), -beta) -1)
        y.append(temp)	
    return y



def g_inverse(t, c, a):
    alpha = (c+a)/float(c)
    return np.power((1 + t/float(a)), -alpha)



def p_k_Beta(x, k, m):
    p_k = sp.stats.beta.cdf(x, k, m-k+1, loc=0, scale=1)
    return p_k


# In[30]:


def hDist_fromBeta(N, m, c, a):
    distribution = []
    for i in range(0, m+1): #i = k in our paper and note h=0 is almost probability 0
        if i == m:
            h = p_k_Beta(g_inverse(i, c, a), i, m)
        elif i==0:
            h = 1 - p_k_Beta(g_inverse(1, c, a), 1, m)
        else:
            h = p_k_Beta(g_inverse(i, c, a), i, m) - p_k_Beta(g_inverse(i+1, c, a), i+1, m)

        distribution.append(h)
    return distribution


def hDist_fromBeta_equals_k(N, i, m, c, a):
 #i = k in our paper and note h=0 is almost probability 0
    if i == m:
        h = p_k_Beta(g_inverse(i, c, a), i, m)
    elif i==0:
        h = 1 - p_k_Beta(g_inverse(1, c, a), 1, m)
    else:
        h = p_k_Beta(g_inverse(i, c, a), i, m) - p_k_Beta(g_inverse(i+1, c, a), i+1, m)
    return h




