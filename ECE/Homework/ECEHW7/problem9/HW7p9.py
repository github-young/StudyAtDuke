#coding: utf-8
"""Created on Wed Oct 25 22:24:53 2017,@author: young"""

import numpy as np
import pylab as pl

f = open('IdVg.txt')
text = f.readlines()
f.close()
dataVd005 = text[4:20]
dataVd1 = text[25:41]

ff = open('IdVd.txt')
text2 = ff.readlines()
ff.close()
dataVg05 = text2[4:19]
dataVg075 = text2[24:39]
dataVg1 = text2[44:59]


def processdata(data):
    newdata = [[],[]]
    for i in range(len(data)):
        newdata[0] += [float(data[i][:20])]
        newdata[1] += [float(data[i][21:-1])]
    return np.array(newdata)
def SlopeGen(data):
    return (data[1][-2]-data[1][-1])/(data[0][-2]-data[0][-1])

VgVd005 = processdata(dataVd005)
VgVd1 = processdata(dataVd1)
VdVg05 = processdata(dataVg05)
VdVg075 = processdata(dataVg075)
VdVg1 = processdata(dataVg1)

slope = SlopeGen(VgVd1)
x = np.linspace(0.82,1,1000)
y = slope*(x-VgVd1[0][-1])+VgVd1[1][-1]

pl.figure(figsize=[6,15])

pl.subplot(311)
pl.plot(VdVg05[0],VdVg05[1],'r-*',label='$V_g$ = 0.5V')
pl.plot(VdVg075[0],VdVg075[1],'g-+',label='$V_g$ = 0.75V')
pl.plot(VdVg1[0],VdVg1[1],'b-x',label='$V_g$ = 1V')
pl.title('$I$-$V_{ds}$ output curve')
pl.xlabel(r'$V_{ds}$ / V')
pl.ylabel(r'$I$ / A')
pl.grid()
pl.legend()

pl.subplot(312)
pl.plot(VgVd1[0],VgVd1[1],'b-*',label='$V_d$ = 1V')
pl.plot(x,y,'b-',linewidth=1,label='linear extrapolation,\nslope=%.3e, $V_T$=%.3fV' %(slope, VgVd1[0][-1]-VgVd1[1][-1]/slope))
pl.plot(VgVd005[0],VgVd005[1],'r-+',label='$V_d$ = 0.05V')
pl.grid()
pl.legend()
pl.title(r'$I$-$V_{gs}$ tranfer curve')
pl.xlabel(r'$V_{gs}$ / V')
pl.ylabel(r'$I$ / A')

pl.subplot(313)
pl.semilogy(VgVd1[0],VgVd1[1],'b-*',label='$V_d$ = 1V')
pl.semilogy(VgVd005[0],VgVd005[1],'r-+',label='$V_d$ = 0.05V')
pl.grid()
pl.legend()
pl.title(r'$log(I)$-$V_{gs}$ sub-threshold curve')
pl.xlabel(r'$V_{gs}$ / V')
pl.ylabel(r'$log(I)$ / log(A)')

pl.savefig('total_p9.pdf')
pl.close()