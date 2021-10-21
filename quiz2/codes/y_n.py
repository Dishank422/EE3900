import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0,10,11,endpoint=True)
y = np.zeros(11)

for i in range(11):
    y[i] = -(1/3)*(1/3)**i+(1/3)*(-1)**i

plt.stem(n,y)
plt.grid()
plt.xlabel("n")
plt.ylabel("y[n]")

plt.show()

