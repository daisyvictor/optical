#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:21:48 2019

@author: sss
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 16:22:34 2018

@author: sss
"""
import numpy as np
from astropy import units as u
from astropy.coordinates import ICRS, Galactic, SkyCoord
from astropy import wcs
from astropy import constants as const
import urllib.request


adress, ra,de,band,q = np.loadtxt('/home/sss/optical/iphas.txt', delimiter='|', 
                                  usecols=(1, 2,3,4,6), unpack=True,dtype=str,skiprows=2)
gl1,gb1 = np.loadtxt('/home/sss/optical/greencatalog',
                                  usecols=(0,1), unpack=True,dtype=str)

print(gl1,gb1,gl1.size)
#print(ra[0:100])
ra=list(map(float,ra))#convert string to float
de=list(map(float,de))

gl1=list(map(float,gl1)) #convert string to float
gb1=list(map(float,gb1))
#print(gl1,gb1)
# convert galactic to icrs 
cg = SkyCoord(l=gl1* u.degree, b=gb1 * u.degree, frame='galactic')
c_icrs = cg.transform_to('icrs')  # c_galactic.icrs does the same thing
ra1=c_icrs.ra.degree
de1=c_icrs.dec.degree

###cinvert list to array
ra=np.array(ra)
de=np.array(de)
ra1=np.array(ra1)
de1=np.array(de1)
print(ra1.size)
count2=0
for index in range(70,ra1.size):
     tf=(abs(ra-ra1[index])<0.20)&(abs(de-de1[index])<0.13)
     in1=np.where(tf>0)
     in1=np.array(in1)
     #print(in1.size)
     #print(ra[in1]) 
     #print(ra1[index])
     #print(de[in1])
     #print(de1[index])
    # print(len(ra[in1]))
     if(len(ra[in1])>0):
        a=np.char.strip(band,' ') 
        q1=np.char.strip(q,' ')
        #print(a[in1])
        #print(q[in1])
        count=0
        #strip:delete certain letter in the beginning and tail;replace(a,'c','d')
        for in2 in range(0,in1.size):
          #print(a[in1[0,in2]])    
          if (a[in1[0,in2]]=='halpha'):
              if(q1[in1[0,in2]]=='true'):
               count=count+1
               print(count)       
               gl1[index]=str(gl1[index])
               gb1[index]=str(gb1[index])
               count1=str(count)
               urllib.request.urlretrieve(adress[in1[0,in2]],'/home/sss/optical/green/G'+gl1[index]+'_'+gb1[index]+'_'+count1+'.fits.fz')
        if(count>0):
            count2=count2+1
print('total available number:',count2)
            #urllib.request.urlretrieve(adress[in1[0,in2]],'/home/sss/optical/green/G'+gl1[index]+'_'+gb1[index]+'_'+count1+'.fits.fz')
 





