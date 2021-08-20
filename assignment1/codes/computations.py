import numpy

A = numpy.array([1,-2,-8])
B = numpy.array([5,0,-2])
C = numpy.array([11,3,7])

def norm(X):
    return((X[0]**2+X[1]**2+X[2]**2)**(0.5))

print("Lambda= ",norm(B-A)/norm(C-B),"=2/3")

