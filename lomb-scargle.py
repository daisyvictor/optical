# -*- coding: utf-8 -*
import numpy as np
# -*- coding: utf-8 -*
import numpy as np
from gatspy.periodic import LombScargleFast
import matplotlib.pyplot as plt
import sys
import os
import math
import scipy.signal as signal
class objects:
    def __init__(self,length,d,m):
        self.length=length
        self.d=d
        self.m=m
        
    def lombscargle(self):
        print(self.length)
        model = LombScargleFast(silence_warnings=True).fit(self.d, self.m, 0.1)
        model.optimizer.period_range = (0.02,min(10,self.length))
        period=model.best_period
        print "period is ",model.best_period
        sco= model.score(period,)
        print "the score is ",sco
        periods, power = model.periodogram_auto(nyquist_factor=2000)##Depend the highest fequency of the model.
        #f=open("tet.txt",'wb')
        #f.write('period is:'+str(period))
        #f.close
        x=periods
        y=power
        fig,axes=plt.subplots(1,2,figsize=(8,8))
        ax1,ax2=axes.flatten()
        ax1.plot(x,y,color="red",linewidth=2)
        ax1.set_xlim(0,10)
        ax1.set_xlabel("period (days)")
        ax1.set_ylabel("Lomb-Scargle Power")
        ax1.legend()
        phase=self.d/(1*period)
        phase=phase%1*1
        ax2.plot(phase,self.m,'ro')
        ax2.set_xlabel("phase")
        ax2.set_ylabel("Mag")
        #ax2.set_ylim(0,1)
        ax2.legend()
       # plt.savefig('/home/yf/ptftry/pic/Lomb-Scargle.png')
        plt.show()
        return period

    def lombscarglescipy(self,period):
        f = np.linspace(0.1, 1000, 10000)
        pgram = signal.lombscargle(self.d, self.m, f)
        periods=2*np.pi/f
        normval = self.d.shape[0]
        power=np.sqrt(4*(pgram/normval))
        x=periods
        y=power
        fig,axes=plt.subplots(1,2,figsize=(8,8))
        ax1,ax2=axes.flatten()
        ax1.plot(x,y,color="red",linewidth=2)
        ax1.set_xlabel("period (days)")
        ax1.set_ylabel("Lomb-Scargle.scipy Power")
        ax1.set_xlim(0,10)
        ax1.legend()
        phase=1.0*self.d/(period)
        phase=phase%1*1
        ax2.plot(phase,self.m,'ro')
        ax2.set_xlabel("phase")
        ax2.set_ylabel("Mag")
        #ax2.set_ylim(0,1)
        ax2.set_xlim(0,1)
        ax2.legend()
       # plt.savefig('/home/yf/ptftry/pic/Lomb-Scargle.png')
        plt.show()
        
        
name=sys.argv[1]
print name
a = np.loadtxt(name) 
print (a.shape[0])
b=a[0:a.shape[0],0]
d=b.T
minn=np.min(b)
length=np.max(b)-minn
m=a[0:a.shape[0],1]
m=m.T

"""
period=2
length=250
d=np.linspace(0,length,num=231)
print d
#d=[1, 1.5,  3, 2, 3.4, 2.5, 6.4, 4.3, 3.2, 2.2, 2.1, 2.3, 2.7, 3.5, 3.6,3.8, 4.5, 4.7,0.1,0.02,0.05,0.07,0.08,1.22,1.25,1.45,1.57,1.46]
#d=np.random.rand(300)
#d=d*1000
#m=1.0*np.sin(2.0*np.pi*d)+1.0/3*np.sin(6.0*np.pi*d)+1.0/5*np.sin(10.0*np.pi*d)+1.0/7*np.sin(14.0*np.pi*d)
#m=np.sin(2*np.pi*d)+np.sin(4*np.pi*d)
m=1.0*np.sin(1.0*2.0*np.pi/period*d)
"""

fig,ax=plt.subplots()
ax.plot(d,m,"ro",linewidth=2)
ax.set_xlabel("period (days)")
ax.set_ylabel("Lomb-Scargle.scipy Power")
ax.legend()
plt.show()


model=objects(length,d,m)
model.lombscargle()
model.lombscarglescipy(2.0*0.289818543008)
