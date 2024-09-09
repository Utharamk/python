num=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    a=int(input("enter the elements:"))
    num.append(a)
num1=str(num)    

num2 = []

for i in range(n):
    flag=0
    for j in range(n):
        if(num1[i]==num1[j] and i != j):
            flag=1
    if(flag == 0):
      num2.append(num1[i])        
      
length=len(num2)     

for i in range(length):
    for j in range(length):
        if(num2[i] > num2[j]):
            largest = num2[i]
            
print(largest)



    


