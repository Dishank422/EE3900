import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0,10,11,endpoint=True)

x = n*np.e**(1j*np.pi*n)

plt.plot(n,np.angle(x))
plt.grid()
plt.xlabel("n")
plt.ylabel("arg(x[n])")

plt.show()

