def grade(avg):
	if avg >= 90:
		return "A+"
	elif avg >= 80:
		return "A"
	elif avg >= 60:
		return "B"
	elif avg >= 45:
		return "C"
	elif avg >= 30:
		return "D"
	else:
		return "F"
		
f = open("students.txt", "r")
out = open("results.txt", "w")

for line in f:
	data = line.split()
	
	name = data[0]
	marks = []
	
	for x in data[1:]:
		marks.append(int(x))
		
	total = sum(marks)
	average = total/len(marks)
	g = grade(average)
	
	out.write("Name: " + name + "\n")
	out.write("Total: " + str(total) + "\n")
	out.write("Average: " + str(round(average,2)) + "\n")
	out.write("Grade: " + g + "\n")
	
f.close()
out.close()

print("Result saved in result.txt")
