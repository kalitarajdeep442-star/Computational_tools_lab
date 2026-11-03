import sqlite3 

con = sqlite3.connect("student.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students(
    roll INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dept TEXT NOT NULL,
    cgpa REAL)""")

while True:
    print("\n1.Add  2.Display  3.Search  4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        try:
            data = (int(input("Roll: ")), input("Name: "),
                    input("Department: "), float(input("CGPA: ")))
            cur.execute("INSERT INTO students VALUES(?,?,?,?)", data)
            con.commit()
            print("Student added.")
        except sqlite3.IntegrityError:
            print("Roll number already exists.")

    elif ch == "2":
        cur.execute("SELECT * FROM students")
        for s in cur.fetchall():
            print(s)

    elif ch == "3":
        r = int(input("Enter Roll: "))
        cur.execute("SELECT * FROM students WHERE roll=?", (r,))
        print(cur.fetchone() or "Student not found.")

    elif ch == "4":
        break

con.close()
