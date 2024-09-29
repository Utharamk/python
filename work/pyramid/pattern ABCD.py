a=int(input("enter the size:"))
for i in range(a):
    for k in range(a-i):
        print(" ",end="")
    for j in range(i+1):
        print(chr(65+j),end=" ")

    print( )


    