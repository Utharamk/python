a=[]
while True:
    print("1.Add task")
    print("2.View all task")
    print("3.Update task")
    print("4.Mark task as completed")
    print("5.Delete")
    print("6.Search task by name")
    print("7.Exit")
    ch=int(input("Enter the choice:"))
    if(ch==1):
        b=[]
        name=input("Enter the name:")
        description=input("Enter the description:")
        date=int(input("Enter the due date:"))
        priority=input("Enter the priority level:")
        b.append(name)
        b.append(description)
        b.append(date)
        b.append(priority)
        b.append(False)
        a.append(b)
        print("Task added successfully")    
    elif ch==2:
        print(a)    


        
    elif ch == 3:
        name = input("Enter task name to update: ")
        for p in a:
            if p[0] == name:
                p[0] = input("Enter new task name: ")
                p[1] = input("Enter new task description: ")
                p[2] = int(input("Enter new task due date: "))
                p[3] = input("Enter new task priority (High, Medium, Low): ")
                print("Task updated successfully!")
                break
        else:
            print("Task not found.")

    elif ch == 4:
        name = input("Enter task name to mark as completed: ")
        for z in a:
            if z[0] == name:
                z[4] = True
                print("Task marked as completed!")
                break
        else:
            print("Task not found.") 
    elif ch==5:
        name = input("Enter task name to delete: ")
        for v in a:
            if v[0] == name:
                a.remove(v)
                print("Task deleted successfully!")
                break
        else:
            print("Task not found.")





    elif ch == 6:
        name = input("Enter task name to search: ")
        for task in a:
            if task[0] == name:
                print("Task Found:")
                print(f"Name: {task[0]}")
                print(f"Description: {task[1]}")
                print(f"Due Date: {task[2]}")
                print(f"Priority: {task[3]}")
                print(f"Completed: {'Yes' if task[4] else 'No'}")
                break
        else:
            print("Task not found.") 
    elif ch == 7:
        print("Exiting the program")
        break                 