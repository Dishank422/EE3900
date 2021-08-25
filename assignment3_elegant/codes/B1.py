import numpy as np

Rinv = np.array([[-0.45, -0.89],[0.89, -0.45]])
B2plus = np.array([-0.38,4.48])
B2minus = np.array([-0.38,-4.48])

print("B1 corresponding to plus = ", np.matmul(Rinv,B2plus))
print("B1 corresponding to minus = ", np.matmul(Rinv,B2minus))

