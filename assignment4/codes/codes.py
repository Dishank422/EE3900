import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,10,100)
Y = X - 5

fig = plt.plot()
plt.plot(X, Y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.savefig("../figures/a")

X = np.linspace(-3,3,100)
Y = np.absolute(X-1)

plt.clf()
plt.plot(X, Y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.savefig("../figures/b")
