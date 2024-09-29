

dict = {}  
while True:
    print("1. Registration")
    print("2. Login")
    print("3. Exit")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        def registration():
            a = input("Enter the name: ")
            b = int(input("Enter the age: "))
            c = int(input("Enter the phone number: "))
            d = input("Enter the Address: ")
            ab = input("Enter the username: ")
            cd = input("Enter the password: ")
            if ab not in dict:
                dict[ab] = {"name": a, "age": b, "phone_no": c, "address": d, "password": cd}
                print("Registration successful")
            else:
                print("Username already exists")
        registration()
    elif ch == 2:
        def login():
            ab = input("Username: ")
            cd = input("Password: ")
            if ab in dict:
                if dict[ab]["password"] == cd:
                    print("Logged in successfully")
                else:
                    print("Invalid password")
            else:
                print("Username does not exist")
        login()
    elif ch == 3:
        print("Exit")
        break