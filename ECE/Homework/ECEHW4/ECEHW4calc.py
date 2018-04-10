#coding: utf-8
"""Created on Sun Oct  1 00:15:02 2017,@author: young"""

import numpy as np

e = 1.6e-19
k = 1.38e-23
T = 300;
Nd = [1e14, 5e16, 1e17]
Na = [1e17, 5e16, 1e17]
ni = [1.5e10, 1.8e6, 2.4e13]
def f(Nd,Na,ni):
    return (k*T)/e*np.log((Nd*Na)/ni**2)

for i in range(3):
    for j in range(3):
        print('%.2f' %f(Nd[i],Na[i],ni[j]))
    print('\n')