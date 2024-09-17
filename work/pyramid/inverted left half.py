n=5
for i in range(n):
    for j in range(n+1):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()