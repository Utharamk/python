# def a_function(string):
#     return len(string)
# print(a_function("Functions"))
# print(a_function("python"))

# def function(n1,n2=20):
#     print("number 1 is:",n1)
#     print("number 2:",n2)
#     print("passing only one argument")
# function(30)

# def function(n1,n2):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
#     print("without using keyword")
# function(n2=50,n1=20)

# def square(num):
#         return num**2
# print("with return statement")
# print(square(52))

# lambda_=lambda argument1,argument2:argument1+argument2
# print("value of the function is:",lambda_(20,30))
# print("value of the function is:",lambda_(40,50))

# def word():
#     string='python function tutorial'
#     x=5
#     def number():
#         print(string)
#         print(x)
#     number()
# word()        

# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return(x*factorial(x-1))
# num=3    
# print(factorial(num))

a={}
even=""
odd=""
for i in range(1,11):
    if i%2==0:
        even=even+str(i)
    else:
        odd=odd+str(i)
a[even]=odd
a={odd:even}
print(a)