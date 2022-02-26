#!/usr/bin/python3.8
import numpy as np 

n=5
xspan = np.array(np.zeros(n))
yspan = np.array(np.zeros(n))
xy = np.stack((xspan, yspan), axis=1)
xy[-1]=1
print(xy)
