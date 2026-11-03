import numpy as np

marks = [78,85,92,67,88,73,95,81,76,89]
temperature = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]
sales = [12500, 13800, 14200, 11900, 15100, 14750, 16000]

data = [marks, temperature, sales]

for values in data:
	arr = np.array(values)
	print("Data:", values)
	print("Mean:", np.mean(arr))
	print("Median:", np.median(arr))
	print("Standard Deviation:", np.std(arr))
	print("Minimum:",np.min(arr))
	print("Maximum:",np.max(arr))
	print()
