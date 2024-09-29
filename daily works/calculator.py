def addition(c,d):
  return c+d
def subtration(c,d):
  return c-d
def multiplication(c,d):
 return c*d
def division(c,d):
 return c/d



while True:
  print("\n1:Addition,\n2:subtration,\n3:multiplication,\n4:division")
  a=int(input("enter your choice:"))
  c=int(input("enther the first number:")) 
  d=int(input("enter the second number:"))
  if(a==1):
   print(c+d)
  elif(a==2):
    print(c-d)
  elif(a==3):
   print(c*d)
  elif(a==4):
   print(c/d)
   break





