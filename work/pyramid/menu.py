a=[]
while True:
    print("\n1.register\n2.login\n3.exit")
    ch=int(input("enter the choice:"))
    if ch==1:
        b=[]
        name=input("enter the name:")
        age=int(input("enter the age:"))
        b.append(name)
        b.append(age)
        a.append(b)
    if(ch==2):
        p=input("enter the name:")
        for i in a:
            i[0]==p
            print(i)    
    if(ch==3):
        break            


    