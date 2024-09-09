a=int(input("Enter the weight:"))
b=int(input("Enter the height:"))
BMI=a/b*2
if(BMI<18.5):
    print("Underweight")
elif(18.5<=BMI<24.9):
    print("Normal weight")
elif(25<=BMI<29.9):
    print("Overweight")
else:
    print("Obese")