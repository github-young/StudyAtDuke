#!/home/young/anaconda3/bin/python
#coding:utf-8
import numpy as np
import pylab as pl
#import seaborn

me = 9.11*10**(-31)
m = me/2
hb = 6.626*10**(-34)/(2*np.pi)
ev = 1.6*10**(-19)

def g3d(E):
    return (2*m/hb**2)**(3/2)*np.sqrt(E)/(2*np.pi**2)


E = np.linspace(0,5,1000)
y3 = g3d(E*ev)*1.6*10**(-25)
y2 = np.array([m/(np.pi*hb*hb)*1.6*10**(-23) for i in range(len(E))])
pl.figure(figsize=[8,16])
pl.subplot(211)
pl.plot(E,y2,'b-',label='2D DOS',linewidth=2.5)
pl.grid()
pl.legend(loc='upper left')
pl.title('2D DOS',fontsize=15)
pl.xlabel('E / eV',fontsize=15)
pl.ylabel(r'DOS / $cm^{-2}eV^{-1}$',fontsize=15)
pl.subplot(212)
pl.plot(E,y3,'r-',label='3D DOS',linewidth=2.5)
pl.grid()
pl.legend(loc='upper left')
pl.title('3D DOS',fontsize=15)
pl.xlabel('E / eV',fontsize=15)
pl.ylabel(r'DOS / $cm^{-3}eV^{-1}$',fontsize=15)
#pl.show()
pl.savefig('HW2plot.pdf')
