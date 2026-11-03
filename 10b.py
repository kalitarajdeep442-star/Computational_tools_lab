A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

rows = len(A)
cols = len(B[0])

addition = [[0 for j in range(cols)]
		for i in range(rows)]
for i in range(rows):
	for j in range(cols):
		addition[i][j] = A[i][j]+B[i][j]
		
subtraction = [[0 for j in range(cols)]
		for i in range(rows)]
for i in range(rows):
	for j in range(cols):
		subtraction[i][j] = A[i][j]-B[i][j]
	
multiplication = [[0 for j in range(cols)]
		for i in range(rows)]
for i in range(rows):
	for j in range(cols):
		for k in range(cols):
			multiplication[i][j] += A[i][k]*B[k][j]
			
transpose = [[0 for j in range(cols)]
		for i in range(rows)]
for i in range(rows):
	for j in range(cols):
		transpose[j][i] = A[i][j]
		
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Transpose:", transpose)
