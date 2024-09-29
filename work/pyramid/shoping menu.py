admins={'ab':'123'}
users={}
products={}
orders=[]

def main_menu():
    while True:
        print("\nMain Menu\n1.Admin\n2.User\n3.Exit\n")
        choice=int(input("Enter choice: "))

        if choice==1:
            admin_section()
        elif choice==2:
            user_section()
        elif choice==3:
            break
        else:
            print("Invalid choice")

def admin_section():
    username=input("Enter admin username: ")
    password=input("Enter admin password: ")
    if username in admins and admins[username]==password:
        print("login successful")
        admin_menu()
    else:
        print("Invalid admin credentials")

def admin_menu():
    while True:
        print("\nAdmin menu\n1.Add product\n2.Update product\n3.Remove product\n4.View products\n5.View orders\n6.Exit")
        choice=int(input("Enter a choice: "))
        if choice==1:
            add_prod()
        elif choice==2:
            update_prod()
        elif choice==3:
            remove_prod()
        elif choice==4:
            view_prod()
        elif choice==5:
            view_orders()
        elif choice==6:
            break
        else:
            print("Invalid choice")

def add_prod():
    prod_id=input("Enter product ID: ")
    if prod_id in products:
        print("Prod_id exists")
        return
    name=input("Enter prod name: ")
    description=input("Enter prod description: ")
    price=float(input("Enter price: "))
    products[prod_id]={'name':name,'description':description,'price':price}
    print("Product added")

def update_prod():
    prod_id=input("Enter product ID for updation: ")
    if prod_id in products:
        name=input("Enter new prod name: ")
        description=input("Enter new prod description: ")
        price=float(input("Enter new price: "))
        products[prod_id]={'name':name,'description':description,'price':price}
        print("Product updated")
    else:
        print("No product")
def remove_prod():
    prod_id=input("Enter product ID for remove: ")
    if prod_id in products:
        del products[prod_id]
        print("Removed")
    else:
        print("No product")

def view_prod():
    if products:
        for prod_id,information in products.items():
            print("ID:",prod_id)
            print("Name:",information['name'])
            print("Description:",information['description'])
            print("Price:",information['price'])
            print()
    else:
        print("No products")

def view_orders():
    if orders:
        for order in orders:
            print(order)
    else:
        print("No orders")


def user_section():
    while True:
        print("\nUser Section\n1.Registe\n2.Login\n3.Exit")
        choice=int(input("Choose an option: "))
        if choice==1:
            register_user()
        elif choice==2:
            login_user()
        elif choice==3:
            break
        else:
            print("Invalid choice, try again.")

def register_user():
    user_id=input("Enter user ID: ")
    if user_id in users:
        print("User ID exists")
        return
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    address=input("Enter your address: ")
    password=input("Enter your password: ")
    users[user_id]={'name':name,'email':email,'address':address,'password':password,'orders':[]}
    print("User registeration done")

def login_user():
    user_id=input("Enter user ID: ")
    password=input("Enter your password: ")
    if user_id in users and users[user_id]['password']==password:
        user_menu(user_id)
    else:
        print("Invalid credentials")

def user_menu(user_id):
     while True:
        print("\nUser Menu")
        print("1.View All Products")
        print("2.Place Order")
        print("3.View Order History")
        print("4.Exit")
        choice=int(input("Choose an option: "))
        if choice==1:
            view_all_products()
        elif choice==2:
            place_order(user_id)
        elif choice==3:
            view_order_history(user_id)
        elif choice==4:
            break
        else:
            print("Invalid choice")

def view_all_products():
    if products:
        for prod_id,information in products.items():
            print("ID:",prod_id)
            print("Name:",information['name'])
            print("Description:",information['description'])
            print("Price:",information['price'])
            print()
    else:
        print("No products")

def place_order(user_id):
    prod_id=input("Enter product ID to order: ")

    if prod_id in products:
        quantity = int(input("Enter quantity: "))
        total_price=products[prod_id]['price']*quantity
        order={'user_id':user_id,'product_id':prod_id,'quantity':quantity,'total_price':total_price,'status':'processing'}
        orders.append(order)
        users[user_id]['orders'].append(order)
        print("Order placed")
    else:
        print("No product")

def view_order_history(user_id):
    if users[user_id]['orders']:
        print("\nOrder history: ")
        for order in users[user_id]['orders']:
            print("Product ID: ",order['product_id'])   
            print("Quantity: ",order['quantity'])
            print("Total Price: ",order['total_price'])
            print("Status: ",order['status'])
    else:
        print("No orders")

main_menu()