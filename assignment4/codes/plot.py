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
