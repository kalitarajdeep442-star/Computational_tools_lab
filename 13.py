import numpy as np
from scipy.integrate import quad

def f(x):
	return x**2
	
x = 3
h = 0.0000001

derivative = (f(x+h)-f(x-h))/(2*h)

integral, error = quad(f,0,3)

print("Function: f(X) = x^2")
print("Numerical derivative at x = ",x," : ",derivative)
print("Numerical Integral from 0 to 3 : ",integral)


