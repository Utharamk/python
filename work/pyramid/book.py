admin = {"admin": "password"}
books = []
users = {}

def main_menu():
    while True:
        print(" Menu:")
        print("1. Admin")
        print("2. User")
        choice = input("Enter your choice: ")
        if choice == "1":
            admin_section()
        elif choice == "2":
            user_section()
        else:
            print("Invalid choice")

def admin_section():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "password":
        while True:
            print("Admin Menu:")
            print("1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. Display All Books")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                add_book()
            elif choice == "2":
                update_book()
            elif choice == "3":
                delete()
            elif choice == "4":
                display()
            elif choice == "5":
                break
            else:
                print("Invalid choice")
    else:
        print("Invalid")

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    quantity = int(input("Enter book quantity: "))
    books.append({"book_id": book_id, "title": title, "author": author, "quantity": quantity})
    print("Book added successfully!")

def update_book():
    book_id = input("Enter book ID: ")
    for book in books:
        if book["book_id"] == book_id:
            title = input("Enter new book title: ")
            author = input("Enter new book author: ")
            quantity = int(input("Enter new book quantity: "))
            book["title"] = title
            book["author"] = author
            book["quantity"] = quantity
            print("Book updated successfully")
            return
    print("Book not found")

def delete():
    book_id = input("Enter book ID: ")
    for book in books:
        if book["book_id"] == book_id:
            books.remove(book)
            print("Book deleted successfully")
            return
    print("Book not found")

def display():
    for book in books:
        print("Book ID:", book["book_id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Quantity:", book["quantity"])
        print()

def user_section():
    while True:
        print("User Menu:")
        print("1. Registration")
        print("2. Login")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        else:
            print("Invalid choice")

def register_user():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")
    username = input("Enter a unique username: ")
    password = input("Enter a password: ")
    if username not in users:
        users[username] = {"name": name, "age": age, "address": address, "phone_number": phone_number, "password": password}
        print("Registration successful")
    else:
        print("Username already exists")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username]["password"] == password:
        while True:
            print("User Menu:")
            print("1. Display")
            print("2. Search Book by Name")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                display()
            elif choice == "2":
                search_book()
            elif choice == "3":
                break
            else:
                print("Invalid choice")
    else:
        print("Invalid username or password")

def search_book():
    title = input("Enter book title: ")
    for book in books:
        if book["title"] == title:
            print("Book ID:", book["book_id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Quantity:", book["quantity"])
            print()
            return
    print("Book not found")
        

main_menu()




