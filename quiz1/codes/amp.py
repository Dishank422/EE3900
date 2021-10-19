import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0,10,11,endpoint=True)

x = n*np.e**(1j*np.pi*n)

plt.plot(n,np.abs(x))
plt.grid()
plt.xlabel("n")
plt.ylabel("|x[n]|")

plt.show()
