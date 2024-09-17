user = {}
x = 1
while True:
    print("\n1.register\n2.login\n3.exit")
    ch = int(input("enter your choice: "))
    if ch == 1:
        username = input("enter your user name:")    
        password = int(input("enter your password:"))
        if username in user:
            print("Username already exists. Please choose another") 
        else:
            user[username] = password
            print("Registered successfully")   
    elif ch == 2:  
        while True:
            username = input("enter your user name:")    
            password = int(input("enter your password:"))
            if username in user and user[username] == password:
                print("Login successfully")
                break
            else:
                print("Invalid")     
    elif ch == 3:
        break
    else:
        print("invalid")
                  
    


    
