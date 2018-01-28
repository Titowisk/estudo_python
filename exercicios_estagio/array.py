# Toy example of arrays in python
import random

# 1 Array
print('1) ------------------------------------')
array = []

for i in range(1, 6):
    array.append(random.randint(1, 10))

print(array, end='\n\n')

# 2 print only the even numbers in an array
print('2) ------------------------------------')
for n in array:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        print("X", end=' ')
print("", end='\n\n')

# 3 print a new array only with even numbers
print('3) ------------------------------------')
array_even = []
for x in array:
    if x % 2 == 0:
        array_even.append(x)
    else:
        array_even.append("X")

print(array_even)
