#coding:utf-8

import numpy as np

e = 1.6e-19
k = 1.38e-23
T = 300
Is = 6e-14
Vo = 0.635
R = 1000

def ID(VD):
    return Is*(np.exp(e*VD/k/T)-1)

print('%.2e' %(ID(Vo)+Vo/R))