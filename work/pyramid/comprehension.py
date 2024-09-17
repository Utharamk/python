a=[]
n=int(input("enter the size:"))
b=input("enter the elements:")
for i in range(n):
    a.append(b)

print(a)
c={x:x*1 for x in range(n) if x==0}
print(c)