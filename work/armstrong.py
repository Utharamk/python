number = int(input("Enter a number: "))
digits = str(number)
length = len(digits)
sum = 0
for i in digits:
    sum += int(i) ** length
if sum == number:
    print("number is an Armstrong number.")
else:
    print("number is not an Armstrong number.")