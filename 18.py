import sqlite3
           
con = sqlite3.connect("employee.db")
cur = con.cursor()

dept = input("Enter Department: ")

cur.execute(
	"SELECT id, name, salary FROM employees WHERE dept=?",(dept,)
)

employees = cur.fetchall()
if employees:
	for e in employees:
		print(e)
else:
	print("Department not found.")

con.close()
