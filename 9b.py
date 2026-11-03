import math

marks = [78,85,92,67,88,73,95,81,76,89]
temperature = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]
sales = [12500, 13800, 14200, 11900, 15100, 14750, 16000]

data = [marks, temperature, sales]

for values in data:
	n = len(values)
	mean = sum(values)/n
	sorted_values = sorted(values)
	if n%2==0:
		median = (sorted_values[n//2-1]+sorted_values[n//2])/2
	else:
		median = sorted_values[n//2]
		
	variance = sum((x-mean)**2 for x in values)/n
	std_dev = math.sqrt(variance)
	
	minimum = min(values)
	maximum = max(values)
	
	print("Data:", values)
	print("Mean:", mean)
	print("Median:", median)
	print("Standard Deviation:", std_dev)
	print("Minimum:", minimum)
	print("Maximum:", maximum)
	print()
