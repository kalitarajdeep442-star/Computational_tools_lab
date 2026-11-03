import sqlite3
           
con = sqlite3.connect("employee.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    designation TEXT NOT NULL,
    dept TEXT NOT NULL,
    salary REAL)""")

while True:
    print("\n1.Add  2.Display  3.Update  4.Delete  5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        try:
            data = (int(input("ID: ")), input("Name: "),
                    input("Designation: "), input("Department: "),
                    float(input("Salary: ")))
            cur.execute("INSERT INTO employees VALUES(?,?,?,?,?)", data)
            con.commit()
            print("Employee added.")
        except sqlite3.IntegrityError:
            print("Employee ID already exists.")

    elif ch == "2":
        cur.execute("SELECT * FROM employees")
        for e in cur.fetchall():
            print(e)

    elif ch == "3":
        i = int(input("ID to update: "))
        data = (input("New Name: "), input("New Designation: "),
                input("New Department: "), float(input("New Salary: ")), i)
        cur.execute("""UPDATE employees
                       SET name=?, designation=?, dept=?, salary=?
                       WHERE id=?""", data)
        con.commit()
        print("Employee updated.")

    elif ch == "4":
        i = int(input("ID to delete: "))
        cur.execute("DELETE FROM employees WHERE id=?", (i,))
        con.commit()
        print("Employee deleted.")

    elif ch == "5":
        break

con.close()
