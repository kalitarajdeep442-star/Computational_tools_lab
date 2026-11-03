from scipy.optimize import minimize
import numpy as np

def f(x):
	return np.sin(x[0])+0.1*x[0]**2
	
x0 = [2]

result = minimize(f,x0)

print("Minimunm point: ",result.x[0])
print("Minimum value: ",result.fun)
