# 
# 
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)



a="ABA"
dic = {x: {y: x + y for y in a} for x in a} 
print(dic)
