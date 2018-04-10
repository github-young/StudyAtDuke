#coding: utf-8
"""Created on Wed Sep 20 23:50:01 2017,@author: young"""

import numpy as np
import pylab as pl

#eV = 1.6e-19
eV = 1

def plotEBand(x,Ev,Eg,dEFi,dEF,i):
    Ec = Ev + Eg
    Emid = Ev + Eg/2
    EFi = Ev + dEFi
    EF = Ev + dEF
    pl.plot(x,Ev,'#00d8ff',ls='-',linewidth=5,label='Ev')
    pl.plot(x,Emid,'-.',linewidth=2,label=r'$E_{midgap}$')
    pl.plot(x,EF,'g--',linewidth=2,label=r'$E_{F}$')
    pl.plot(x,EFi,'k',ls=':',linewidth=2,label=r'$E_{Fi}$')
    pl.plot(x,Ec,'r-',linewidth=5,label=r'$E_{c}$')
    pl.title('Energy Band Diagram for part %s' %(i+1))
    pl.ylabel('E / eV')
    pl.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off
    pl.legend(bbox_to_anchor=(0.4,0.5),fontsize=8)
    pl.grid()
#    pl.show()
    return 0
def genData():
    x = np.linspace(0,10,1000)
    Ev = x*0
    return x,Ev

x,Ev = genData()
Eg = np.array([1.12,1.12,1.12,1.08,1.015])*eV
dEFi = np.array([-7.3,-7.3,-7.3,-11.0,-15.8])*eV*1e-3
dEF = np.array([298.8,-358.4,298.8,25.8,0.54])*eV*1e-3

for i in range(5):
#    pl.subplot(3,2,i+1)
    pl.figure(figsize=[5,4])
    plotEBand(x,Ev,Eg[i],dEFi[i],dEF[i],i)
#    pl.show()
    pl.savefig('HW3_plot_%s.pdf' %i)
#    pl.savefig('hw3_plot.pdf')
    pl.close()

#plotEBand(x,Ev,Eg[0],dEFi[0],dEF[0],0)