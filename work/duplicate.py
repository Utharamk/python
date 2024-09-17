a=int(input("enter the size:"))
num=[]
for i in range(a):
    b=int(input("enter the elelments:"))
    num.append(b)
print(num)
dict = {}
for i in a:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)



    


