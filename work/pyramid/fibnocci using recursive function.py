def fibnocci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibnocci(n-1)+fibnocci(n-2)
n=int(input("enter a number:"))    
print(fibnocci(n-1))    
    

    