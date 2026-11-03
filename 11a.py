import numpy as np
A = np.array([[4,7],[2,6]])

print("Matrix:")
print(A)

det = np.linalg.det(A)
print("\nDeterminant:",det)

if det!=0:
	inverse = np.linalg.inv(A)
	print("\nInverse:")
	print(inverse)
else:
	print("\nInverse does not exist.")

rank = np.linalg.matrix_rank(A)
print("\nRank:", rank)
