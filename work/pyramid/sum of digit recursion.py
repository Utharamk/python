def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
print("Sum of digits of 12345 is:", sum_of_digits(12345))


    