class Library:
    def __init__(self): 
        self.admincredential = {"username": "abc", "password": "123"} 
        self.users = []
        self.books = []
    
    def main_menu(self):
        print("1. Admin")
        print("2. User")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            self.admin_section()
        elif choice == 2:
            self.user_section()  
        else:
            print("Invalid choice")
    
    def admin_section(self):
        username = input("Enter the Username: ")
        password = input("Enter the Password: ")
        if username == self.admincredential["username"] and password == self.admincredential["password"]:  
            self.admin_menu()
        else:
            print("Invalid credentials")
            self.admin_section()
    
    def admin_menu(self):
        print("ADMIN MENU")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Display All Books")
        print("5. Exit")
        choice1 = int(input("Enter the choice: "))
        if choice1 == 1:
            self.addbook()
        elif choice1 == 2:
            self.updatebooks()
        elif choice1 == 3:
            self.deletebooks()
        elif choice1 == 4:
            self.display_all_books()
        elif choice1 == 5:
            print("Exit")
            self.main_menu()
    
    def addbook(self):
        book_id = int(input("Enter the Book ID: "))
        title = input("Enter the Title: ")
        author = input("Enter the Author: ")
        quantity = int(input("Enter book quantity: "))
        book = {"book_id": book_id, "title": title, "author": author, "quantity": quantity}
        self.books.append(book)
        print("Book Added Successfully")
        self.admin_menu()
    
    def updatebooks(self):
        book_id = int(input("Enter the Book ID: "))
        for book in self.books:
            if book["book_id"] == book_id:
                title = input("Enter the new title: ")
                author = input("Enter the new author: ")
                quantity = int(input("Enter the new quantity: "))
                book["title"] = title
                book["author"] = author
                book["quantity"] = quantity
                print("Book Updated Successfully")
                self.admin_menu()
                return  
        print("Book not found")
        self.admin_menu()
    
    def deletebooks(self):
        book_id = int(input("Enter the Book ID: "))
        for book in self.books:
            if book["book_id"] == book_id:
                self.books.remove(book)
                print("Book Deleted Successfully")
                self.admin_menu()
                return  
        print("Book not found")
        self.admin_menu()
    
    def display_all_books(self):
        if not self.books:
            print("No books available")  
        else:
            for book in self.books:
                print(f"Book ID: {book['book_id']}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Quantity: {book['quantity']}")
                
        self.admin_menu()
lib = Library()
lib.main_menu()