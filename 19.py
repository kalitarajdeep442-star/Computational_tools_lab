import tkinter as tk
from tkinter import ttk, messagebox
from database import Database

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("900x500")
        
        self.db = Database()

        # Variables
        self.book_id_var = tk.StringVar()
        self.title_var = tk.StringVar()
        self.author_var = tk.StringVar()
        self.member_var = tk.StringVar()

        self.setup_ui()
        self.populate_treeview()

    def setup_ui(self):
        # Left Frame: Data Entry Form
        form_frame = tk.LabelFrame(self.root, text="Library Operations", padx=10, pady=10)
        form_frame.place(x=20, y=20, width=350, height=450)

        tk.Label(form_frame, text="Book ID:").grid(row=0, column=0, pady=10, sticky="w")
        tk.Entry(form_frame, textvariable=self.book_id_var, width=30).grid(row=0, column=1, pady=10)

        tk.Label(form_frame, text="Title:").grid(row=1, column=0, pady=10, sticky="w")
        tk.Entry(form_frame, textvariable=self.title_var, width=30).grid(row=1, column=1, pady=10)

        tk.Label(form_frame, text="Author:").grid(row=2, column=0, pady=10, sticky="w")
        tk.Entry(form_frame, textvariable=self.author_var, width=30).grid(row=2, column=1, pady=10)

        tk.Label(form_frame, text="Member (Issue):").grid(row=3, column=0, pady=10, sticky="w")
        tk.Entry(form_frame, textvariable=self.member_var, width=30).grid(row=3, column=1, pady=10)

        # Buttons
        btn_frame = tk.Frame(form_frame)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20)

        tk.Button(btn_frame, text="Add Book", width=12, command=self.add_book).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Issue Book", width=12, command=self.issue_book).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Return Book", width=12, command=self.return_book).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Search", width=12, command=self.search_book).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="View All", width=12, command=self.populate_treeview).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Clear Fields", width=12, command=self.clear_fields).grid(row=2, column=1, padx=5, pady=5)

        # Right Frame: Data Display
        display_frame = tk.Frame(self.root)
        display_frame.place(x=390, y=20, width=490, height=450)

        scroll_y = ttk.Scrollbar(display_frame, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(display_frame, columns=("ID", "Title", "Author", "Status", "Issued To"), 
                                 yscrollcommand=scroll_y.set, show="headings")
        
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_y.config(command=self.tree.yview)

        for col, width in zip(self.tree["columns"], [60, 150, 120, 70, 90]):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<ButtonRelease-1>", self.on_tree_click)

    def add_book(self):
        b_id, title, author = self.book_id_var.get(), self.title_var.get(), self.author_var.get()
        if not all([b_id, title, author]):
            messagebox.showwarning("Input Error", "ID, Title, and Author are required.")
            return

        if self.db.add_book(b_id, title, author):
            self.populate_treeview()
            self.clear_fields()
            messagebox.showinfo("Success", "Book added successfully.")
        else:
            messagebox.showerror("Error", "Book ID already exists.")

    def issue_book(self):
        b_id, member = self.book_id_var.get(), self.member_var.get()
        if not all([b_id, member]):
            messagebox.showwarning("Input Error", "Book ID and Member name required for issuing.")
            return

        status = self.db.issue_book(b_id, member)
        if status == "Success":
            self.populate_treeview()
            self.clear_fields()
            messagebox.showinfo("Success", f"Book {b_id} issued to {member}.")
        elif status == "Issued":
            messagebox.showwarning("Warning", "Book is already issued out.")
        else:
            messagebox.showerror("Error", "Book not found.")

    def return_book(self):
        b_id = self.book_id_var.get()
        if not b_id:
            messagebox.showwarning("Input Error", "Book ID required to return.")
            return

        status = self.db.return_book(b_id)
        if status == "Success":
            self.populate_treeview()
            self.clear_fields()
            messagebox.showinfo("Success", f"Book {b_id} returned successfully.")
        elif status == "Available":
            messagebox.showwarning("Warning", "Book is already in the library.")
        else:
            messagebox.showerror("Error", "Book not found.")

    def search_book(self):
        query = self.book_id_var.get() or self.title_var.get() or self.author_var.get()
        if not query:
            messagebox.showwarning("Input Error", "Enter ID, Title, or Author to search.")
            return
        
        rows = self.db.search_book(query)
        self.update_treeview(rows)

    def populate_treeview(self):
        self.update_treeview(self.db.fetch_all())

    def update_treeview(self, rows):
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def on_tree_click(self, event):
        selected = self.tree.focus()
        values = self.tree.item(selected, 'values')
        if values:
            self.clear_fields()
            self.book_id_var.set(values[0])
            self.title_var.set(values[1])
            self.author_var.set(values[2])
            self.member_var.set(values[4] if values[4] else "")

    def clear_fields(self):
        self.book_id_var.set("")
        self.title_var.set("")
        self.author_var.set("")
        self.member_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
