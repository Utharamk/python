bill=int(input("Enter the number:"))
units=0
if bill<=100:
    units=bill*5
elif(bill<=200):
    units=100*5+(bill-100)*10
else:
    units=100*5+100*10+(bill-200)*15

print(units)


