a = []
b = []
c = []
for i in range(1, 11):
    if (i % 2 == 0):
        a.append(str(i))
    else:
        b.append(str(i))
odd_str = ""
even_str = ""
for num in b:
    odd_str += num
for num in a:
    even_str += num
print("{" + odd_str + ":" + even_str + "}")

 
    

       
     
    
    

       


    
