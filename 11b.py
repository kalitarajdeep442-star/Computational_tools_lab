A = [[4,2],[2,6]]

a = A[0][0]
b = A[0][1]
c = A[1][0]
d = A[1][1]

det = a*d-b*c

print("Matrix:")
for row in A:
	print(row)
	
print("\nDeterminant:", det)

if det == 0:
	print("Inverse does not exist.")
else:
	inverse = [[d/det, -b/det],[-c/det, a/det]]
	print("\nInverse:")
	for row in inverse:
		print(row)
		
if det!=0:
	rank = 2
elif a!=0 or b!=0 or c!=0 or d!=0:
	rank = 1
else:
	rank = 0
print("\nRank:",rank)



