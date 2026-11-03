class LibraryItem:
	def __init__(self, title):
		self.title = title
		self.issued = False
		
	def display(Self):
		print("Title:", self.title)
		
	def issue(self):
		if not self.issued:
			self.issued = True
			print(self.title, " has been issued.")
		else:
			print(self.title, " is already issued.")
			
	def return_item(self):
		if self.issued:
			self.issued = False
			print(self.title, " has been return.")
		else:
			print(self.title, " was not issued.")
			
class Book(LibraryItem):
	def display(self):
		print("Book: ", self.title)
		
class Magazine(LibraryItem):
	def display(self):
		print("Magazine: ", self.title)
		
class Journal(LibraryItem):
	def display(self):
		print("Journal: ", self.title)	
		
book = Book("Python Programming")
magazine = Magazine("India Today")
journal = Journal("Computer Science Journal")

items = [book, magazine, journal]

print("Library Items:")
for item in items:
	item.display()

print("\nIssued Operations:")
book.issue()
magazine.issue()
journal.issue()

print("\nReturn Operations:")
book.return_item()
magazine.return_item()
journal.return_item()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

			
