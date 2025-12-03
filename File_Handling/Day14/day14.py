# LMS
# 1. Add Book
# 2. Update, remove, view books
# by OOP


class LMS:
    books = []
    def add_book(self, name, author, pages, type):
        self.name = name
        self.author = author
        self.pages = pages
        self.type = type
        self.books.append(self.name)
        
    def update_book(self,name,new_name):
        if name in self.books:
            index = self.books.index(name)
            self.books.pop(index)
            self.books.insert(index,new_name)
            print(f"{name} book updated to {new_name}")
        else:
            print("Book not found.")
            
            
    def remove_book(self,name):
        if name in self.books:
            index = self.books.index(name)
            self.books.pop(index)
            print(f"{name} book removed.")
        else:
            print("Book not found.")
            
    def view_books(self):
        print("Books are: \n")
        for book in self.books:
            print(book)
            

while True:
    choice = int(input("Enter 1 to add book, 2 to update book, 3 to remove book, 4 to view book, 5 to exit: "))
    library1 = LMS()
    
    match choice:
        case 1:
            name = input("Enter a book name: ")
            author = input("Enter a book name: ")
            pages = input("Enter a book name: ")
            type = input("Enter a book name: ")
            library1.add_book(name, author, pages, type)
            print("Book added.")
            
        case 2:
            name = input("Enter the name to update: ")
            new_name = input("ENter the new name: ")
            library1.update_book(name, new_name)
            
        case 3:
            name = input("Enter the name of book to remove: ")
            library1.remove_book(name)
            
        case 4:
            library1.view_books()
        
        case 5:
            break
        
        case _:
            print("Invalid Input")