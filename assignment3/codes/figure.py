#Code by GVV Sharma
#November 19, 2019
#released under GNU GPL
import matplotlib.pyplot as plt
import numpy as np

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from coeffs import * 

#setting up plot
fig = plt.figure()

#Points on the plane
A = np.array([2.5,4.9]).reshape((2,1))
B = np.array([-0.375,4.48]).reshape((2,1))
C = np.array([0,0]).reshape((2,1))
D = np.array([5,0]).reshape((2,1))

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)

#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],label="AB")
plt.plot(x_BC[0,:],x_BC[1,:],label="BC")
plt.plot(x_CD[0,:],x_CD[1,:],label="CD")
plt.plot(x_DA[0,:],x_DA[1,:],label="DA")

#plotting point
plt.scatter(A[0],A[1])
plt.scatter(B[0],B[1])
plt.scatter(C[0],C[1])
plt.scatter(D[0],D[1])
plt.text(2.5,4.9, "A", color='red')
plt.text(-0.375,4.48, "B", color='red')
plt.text(0,0, "C", color='red')
plt.text(5,0, "D", color='red')

#save plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');
plt.grid()
plt.savefig('../figures/figure.png')
