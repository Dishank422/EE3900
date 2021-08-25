import numpy as np

R = np.array([[-0.45, 0.89],[-0.89, -0.45]])
D1 = np.array([-2.27,4.45])

print("D2 = ", np.matmul(R,D1))
