elements = []
n=int(input("enter the number of elements:"))
for i in range(n):
    a=int(input("enter the elements:"))
    elements.append(a)
frequency = {}
for i in elements:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)