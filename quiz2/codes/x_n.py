import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(-10,10,21,endpoint=True)
x = np.zeros(21)

for i in range(10):
    x[i] = 1

for i in range(11):
    x[i+10] = (1/2)**(i)

plt.stem(n,x)
plt.grid()
plt.xlabel("n")
plt.ylabel("x[n]")

plt.show()
