student1 = ("S1", "Rohan")
student2 = ("S2", "Rahul")

course_1 = {"Python", "Math", "Physics", "English"}
course_2 = {"Python", "Biology", "Chemistry", "Physics"}

print("Student 1:", student1)
print("Student 2:", student2)

print("\nCourses of Student 1:", course_1)
print("\nCourses of Student 2:", course_2)

print("\nAll Courses(union):")
print(course_1.union(course_2))

print("\nCommon Courses(intersection):")
print(course_1.intersection(course_2))

print("\nCourses only in student 1:")
print(course_1.difference(course_2))

print("\nCourses only in student 2:")
print(course_2.difference(course_1))
