"""
import numpy as np
import matplotlib.pyplot as plt
fig = plt.plot()

y, x = np.ogrid[-3:5:1000j, -4:8:1000j]
plt.contour(
    x.ravel(), y.ravel(), y**2 - 4*x -2*y + 5, [0])
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("../figures/figure.png")

def parab_gen(y,a):
	x = y**2/a
	return x
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

fig = plt.figure()
len = 100
y = np.linspace(-4,4,len)

def parab_gen(y,a):
    x = y**2/a
    return x

V = np.array(([0,0],[0,1]))
u = np.array(([-2,-1]))
f = 5

O = np.array(([0,0]))

D_vec,P = LA.eig(V)
D = np.diag(D_vec)

p = P[:,0]
eta = 2*u@p

foc = eta/D_vec[1]

x = parab_gen(y,foc)

cA = np.vstack((u+eta*0.5*p,V))
cb = np.vstack((-f,(eta*0.5*p-u).reshape(-1,1)))
c = LA.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()
P=-P

c1 = np.array(([(u@V@u-2*D_vec[0]*u@u+D_vec[0]**2*f)/(eta*D_vec[0]**2),0]))
xStandardparab = np.vstack((x,y))

xActualparab = P@xStandardparab + c[:,np.newaxis]

plt.plot(xActualparab[0,:],xActualparab[1,:],label='Given Parabola',color='r')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
