# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:56:36 2024

@author: Student
"""
import numpy as np
from matplotlib import pyplot as plt


# step 1: start

# step 2: Define function
def f(x):
    return x*x - 5.0*x + 6.0

# step 3: choose initial guess x0 and x1
x0 = 1.5
x1 = 2.2 #print(f(x0)*f(x1))

# step 4: error tolerance
e = 1e-10

root = [];
i = 0;
while (True):
    # step 5
    x2 = (x0 + x1) /2.0
    # step 6
    if f(x0)*f(x2) < 0:
        x0 = x0
        x1 = x2  
    elif f(x0)*f(x2) > 0:
        x0 = x2
        x1 = x1

    root.append(x2)    
    print("i = ", i, "; x2 = ", x2)
    i = i+1
    
    if (f(x0)*f(x2)==0 or abs(f(x2))<e):
        print("go to step 8")
        break

# step 8
print("Display x2 = ", x2, " ", f(x2))

plt.plot(root,"-")
plt.plot(0,root[0],"*b")
    