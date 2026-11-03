students = []

while True:
	print("\n---- Student Record Management----")
	print("1. Insert student")
	print("2. Delete student")
	print("3. Search student")
	print("4. Display all student")
	print("5. Exit")
	
	choice = int(input("Enter your choice: "))
	if choice == 1:
		roll = input("Enter Roll Number: ")
		name = input("Enter Name: ")
		age = int(input("Enter Age: "))
		marks = int(input("Enter Marks: "))
		
		student = {
			"Roll": roll,
			"Name": name,
			"Age": age,
			"Marks": marks
		}
		students.append(student)
		print("Student record inserted succesfully.")
		
	elif choice == 2:
		roll = input("Enter Roll Number to delete: ")
		found = False
		for student in students:
			if student["Roll"] == roll:
				students.remove(student)
				found = True
				print("Students record deleted.")
				break
		if not found:
			print("Student not found.")
			
	elif choice == 3:
		roll = input("Enter Roll Number to search: ")
		found = False
		for student in students:
			if student["Roll"] == roll:
				print("\nStudent Found:")
				print("Roll :",student["Roll"])
				print("Name :",student["Name"])
				print("Age :",student["Age"])
				print("Marks :",student["Marks"])
				found = True
				break
				
		if not found:
			print("Student not found.")
	
	elif choice == 4:
		if len(students) == 0:
			print("No student records available.")
		else:
			print("\nStudent records:")
			for student in students:
				print(student)
				
	elif choice == 5:
		print("Program ended.")
		break
		
	else:
		print("Invalid Choice!")
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

