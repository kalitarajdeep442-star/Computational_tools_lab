import numpy as np

mid = np.array([
	[65,70,68,72],
	[78,75,80,77],
	[55,60,58,62],
	[82,85,80,88],
	[70,68,72,74]
])

end = np.array([
	[72,78,75,80],
	[84,82,86,83],
	[65,68,66,70],
	[88,90,85,92],
	[78,75,80,82]
])

students = ["S1", "S2", "S3", "S4", "S5"]

midTotal = np.sum(mid, axis=1)
endTotal = np.sum(end, axis=1)

midAverage = np.mean(mid, axis=1)
endAverage = np.mean(end, axis=1)

improvement = ((endTotal-midTotal)/midTotal)*100

print("Student  Mid Total  End Total  Mid Average  End Average  Improvement")

for i in range(len(students)):
	print(f"{students[i]}       {midTotal[i]}         {endTotal[i]}         {midAverage[i]:.2f}        {endAverage[i]:.2f}       {improvement[i]:.2f}%")

