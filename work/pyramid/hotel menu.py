admin={"Username":"admin","Password":"123"}
receptionist={"Username":"res","Password":"111"}

rooms={}
guests={}
Reservations={}

g_c=1
r_c=1


def Main_menu():
    while True:
        print("1.Admin")
        print("2.Receptionist")
        print("3.Guest")
        ch=int(input("Enter the choice:"))
        if ch==1:
            Admin()
        elif ch==2:
            receptionist()
        elif ch==3:
            Guest()
        elif ch==4:
            print("Exit")
            break    
        else:
            print("Invalid")
            

def Admin():
    username=input("Enter username of admin: ")
    password=input("Enter password of admin: ")
    if admin.get(username)==password:
        admin()
    else:
        print("Invalid Admin credentials.")


def Admin_menu() :
    while True:
        print("Admin menu")
        print("1.Add room")
        print("2.Update room Details")
        print("3.Remove room")
        print("4.View all reservations")
        print("5.Generate reports")
        print("6.Exit")
        ch=int(input("Enter the choice:"))
        if ch == "1":
            add_room()
        elif ch == "2":
            update_room_details()
        elif ch == "3":
            remove_room()
        elif ch == "4":
            view_all_reservations()
        elif ch == "5":
            generate_reports()
        elif ch == "6":
            break
        else:
            print("Invalid")
            admin()

def add_room():
    while True:
        room_number=input("Enter room number: ")
        if room_number in rooms:
            print("Room exists")
        else:
            break
    room_types=["single","double","suite"]
    while True:
        room_type=input("Enter room type(single/double/suite:").lower()
        if room_type in room_types:
            break
        else:
            print("Invalid room type")
    price=input("Enter price per night: ")
    rooms[room_number]={'type':room_types,'price':price,'status':'available'}
    print(f"Room {room_number} has added.")



    
    



def update_room_details():
    room_number = int(input("Enter room number: "))
    for room in rooms:
        if room["room_number"] == room_number:
            room_type = input("Enter new room type (single, double, suite): ")
            price = int(input("Enter new price per night: "))
            room["type"] = room_type
            room["price"] = price
            print("updated successfully")
            Admin_menu()

def remove_room():
     room_number = int(input("Enter room number: "))
     for room in rooms:
        if room["room_number"] == room_number:
            rooms.remove(room)
            print("removed successfully.")
            Admin_menu()
            return
        print("room not found")
        Admin_menu()

def view_all_reservations() :
     for reservation in Reservations:
        print(f"Guest ID: {reservation['guest_id']}, Room Number: {reservation['room_number']}, Check-in Date: {reservation['check_in_date']}, Check-out Date: {reservation['check_out_date']}")
        Admin_menu()



            

def generate_reports():
    total_rooms=len(rooms)
    occupied_rooms=sum(1 for room in rooms.values() if room['status']=='occupied')
    available_rooms=sum(1 for room in rooms.values() if room['status']=='available')
    reserved_rooms=total_rooms-occupied_rooms -available_rooms
    revenue=sum(float(room['price']) for room in rooms.values() if room['status']=='occupied')

    print(f"Total Rooms: {total_rooms}")
    print(f"Occupied Rooms: {occupied_rooms}")
    print(f"Available Rooms: {available_rooms}")
    print(f"Reserved Rooms: {reserved_rooms}")
    print(f"Total Revenue: {revenue:.2f}")



   

    

def receptionist():
    username=input("Enter the username:")
    password=int(input("Enter the password:"))
    if username==receptionist[username] and password==receptionist[password]:
        receptionist_menu()
    else:
        print("Invalid")
        receptionist()

def receptionist_menu():
    while True:
        print("1. Check-In Guest")
        print("2. Check-Out Guest")
        print("3. Make Reservation")
        print("4. Cancel Reservation")
        print("5. View Available Rooms")
        print("6. View Guest Details")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
         check_in_guest()
        elif choice == "2":
         check_out_guest()
        elif choice == "3":
         make_reservation()
        elif choice == "4":
         cancel_reservation()
        elif choice == "5":
         view_available_rooms()
        elif choice == "6":
         view_guest_details()
        elif choice == "7":
         break
        else:
         print("Invalid")
        receptionist_menu()

def check_in_guest():
    guest_id=input("Enter guest ID: ")
    room_number=input("Enter room number: ")
    if room_number in rooms and rooms[room_number]['status']=='reserved':
        rooms[room_number]['status']='occupied'
        print(f"Guest {guest_id} checked into room {room_number}")
    else:
        print("Room not reserved.")


def check_out_guest():
     room_number = input("Enter room number: ")
     guest_id=input("Enter guest ID: ")
     if room_number in rooms and rooms[room_number]['status']=='occupied':
        rooms[room_number]['status']='available'
        print(f"Guest {guest_id} checked out from room {room_number}")
     else:
        print("Room not occupied.")


def make_reservation():
        global r_c
        guest_id = int(input("Enter guest id: "))
        room_number = int(input("Enter room number: "))
        check_in_date = input("Enter check-in date: ")
        check_out_date = input("Enter check-out date: ")
        for room in rooms:
            if room["room_number"] == room_number:
                room["availability"] = "reserved"
                Reservations.append({"guest_id": guest_id, "room_number": room_number, "check_in_date": check_in_date, "check_out_date": check_out_date})
                print("Reservation made successfully.")
                receptionist_menu()
                return
            print("Room not found.")
            receptionist_menu()

def cancel_reservation():
    reservation_id = int(input("Enter reservation ID: "))
    for reservation in Reservations:
        if reservation["reservation_id"] == reservation_id:
            Reservations.remove(reservation)
            print("Reservation cancelled successfully.")
            receptionist_menu()

def view_available_rooms():
    available_rooms=[room_num for room_num, details in rooms.items() if details['status']=='available']
    if available_rooms:
        for room in available_rooms:
            print(f"Room {room}:{rooms[room]}")
    else:
        print("No rooms")

def view_guest_details():
    if guests:
        for g_id,details in guests.items():
            print(f"Guest ID:{g_id},Name:{details['name']},Contact:{details['contact']}")
    else:
        print("No guest found")


def guest():
     while True:
         print("Guest Menu")
         print("1. Register")
         print("2. Login")
         ch=int(input("Enter your choice:"))
         if ch==1:
             register()
         elif ch==2:
             login()
         elif ch==3:
             break      
         else:
             print("Invalid choice")
             guest()
def register():
     global g_c
     while True:
        g_id=input("Enter guest ID: ")
        if g_id not in guests:
            print("Invalid guest ID")
        else:
            break
        name=input("Enter name: ")
        contact=input("Enter contact details: ")
        address=input("Enter address: ")
        username=input("Enter username: ")
        if guests.get(username)==password:
            guest_menu()
        else:
            print("Invalid username.")
        return
     password=input("Enter password: ")
     guests[g_c]={'name':name,'contact':contact,'address':address,'username':username,'password':password}
     print(f"Registration successful. Your Guest ID is {g_c}")
     g_c+=1

def login():
     username = input("Enter your username: ")
     password = input("Enter your password: ")
     for guest in guests:
          if guest["username"]==username and guest["password"]==password:
               print("Guest logged in successfully")
               guest()
               return
     print("Invalid")
     


def guest_menu(username):
    while True:
        print("Guest Menu:")
        print("1. View Available Rooms")
        print("2. Make a Reservation")
        print("3. View Reservation Status")
        print("4. Update Personal Information")
        print("5. Cancel Reservation")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_available_rooms()
        elif choice == "2":
            make_reservation(username)
        elif choice == "3":
            view_reservation_status(username)
        elif choice == "4":
            update_personal_info(username)
        elif choice == "5":
            cancel_reservation(username)
        elif choice == "6":
            print("Exiting guest menu...")
            break
        else:
            print("Invalid choice.")


def view_reservation_status(g_id):
    guest_reservations=[res for res in Reservations.values() if res['guest_id']==g_id]
    if guest_reservations:
        for res in guest_reservations:
            print(f"Room {res['room_number']},check-in:{res['check_in']},check-out:{res['check_out']},status:{res['status']}")
    else:
        print("empty reservation.")

def update_personal_information(g_id):
    contact=input("Enter new contact details: ")
    address=input("Enter new address: ")
    guests[g_id]['contact']=contact
    guests[g_id]['address']=address
    print("updated successfully.")

def cancel_guest_reservation(g_id):
    guest_reservations=[res_id for res_id, res in Reservations.items() if res['g_id'] == g_id]
    if guest_reservations:
        for res_id in guest_reservations:
            room_number = Reservations[res_id]['room_number']
            rooms[room_number]['status']='available'
            del Reservations[res_id]
        print("cancelled successfully.")
    else:
        print("No reservations.")

  
Main_menu()    


