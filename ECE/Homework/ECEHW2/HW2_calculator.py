#!/usr/bin/python3
#coding:utf-8

import numpy as np

#problem 7
def f(ms,T):
    return (2*ms*9.11e-31*2*1.38e-23*T/(6.626e-34/(2*np.pi))**2)**(3/2)/(3*np.pi**2)
#problem 9
def ff(E,EF):
    E = E*1.6e-19
    EF = EF*1.6e-19
    return 1/(1+(np.exp((E-EF)/(1.38e-23*300))))

print(ff(1.11,1.11/2),ff(0.66,0.33),ff(1.43,1.43/2))
print(1-ff(0,1.11/2),1-ff(0,0.33),1-ff(0,1.43/2))
