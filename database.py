import sqlite3

class Database:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                book_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                status TEXT NOT NULL,
                issued_to TEXT
            )
        ''')
        self.conn.commit()

    def add_book(self, book_id, title, author):
        try:
            self.cursor.execute("INSERT INTO books VALUES (?, ?, ?, 'Available', '')", (book_id, title, author))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False # Book ID already exists

    def issue_book(self, book_id, member_name):
        self.cursor.execute("SELECT status FROM books WHERE book_id=?", (book_id,))
        result = self.cursor.fetchone()
        
        if result and result[0] == 'Available':
            self.cursor.execute("UPDATE books SET status='Issued', issued_to=? WHERE book_id=?", (member_name, book_id))
            self.conn.commit()
            return "Success"
        elif result:
            return "Issued"
        return "Not Found"

    def return_book(self, book_id):
        self.cursor.execute("SELECT status FROM books WHERE book_id=?", (book_id,))
        result = self.cursor.fetchone()
        
        if result and result[0] == 'Issued':
            self.cursor.execute("UPDATE books SET status='Available', issued_to='' WHERE book_id=?", (book_id,))
            self.conn.commit()
            return "Success"
        elif result:
            return "Available"
        return "Not Found"

    def search_book(self, query):
        search_term = f"%{query}%"
        self.cursor.execute("SELECT * FROM books WHERE book_id LIKE ? OR title LIKE ? OR author LIKE ?", 
                            (search_term, search_term, search_term))
        return self.cursor.fetchall()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
