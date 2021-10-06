import numpy as np

def integral(func, x, a, b):
    index = 0
    while(x[index] < a):
        index += 1
    integral = 0
    while(x[index] < b):
        integral += (func[index+1]+func[index])*(x[index+1]-x[index])/2
        index += 1
    return integral

omega = np.linspace(-2*np.pi-1,2*np.pi+1,100000)
y = 1/(1-(5/6)*(np.exp(-1j*omega))) +  1/(1-(6/5)*(np.exp(-1j*omega)))

amp = (y*np.conj(y))**(0.5)

print(integral(amp, omega, 0, np.pi))

