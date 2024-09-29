number = int(input("Enter a number: "))

def is_disarium(number):
    num_str = str(number)
    sum = 0
    for i, digit in enumerate(num_str):
        sum += int(digit) ** (i + 1)
    return sum == number
print(is_disarium(number))