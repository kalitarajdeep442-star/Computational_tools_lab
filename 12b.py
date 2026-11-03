import numpy as np

A = np.array([[4,10],[5,6]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Matrix: ",A)
print("\nEigenValues: ",eigenvalues)
print("\nEigenVectors: ", eigenvectors)
