# Toy example of matrixs in python

import random


# 1 Simple example
matrix = []

columns = 5
lines = 5

print("1) -----------------------", end='\n\n')

print('Matrix {}x{}'.format(lines, columns))
for i in range(columns):
    matrix.append([])
    for n in range(lines):
        matrix[i].append(random.randint(1, 10))
    print(matrix[i])

print('')

# 2 prints only the even numbers in an matrix

matrix = []


print("2) -----------------------", end='\n\n')

for i in range(columns):
    matrix.append([])
    for n in range(lines):
        r_input = random.randint(1, 10)
        if r_input % 2 == 0:
            matrix[i].append(r_input)
        else:
            matrix[i].append('X')
    print(matrix[i])

print('')
# 3 Prints an identity matrix

matrix = []


print("3) -----------------------", end='\n\n')
if columns == lines:
    for i in range(columns):
        matrix.append([])
        for n in range(lines):
            r_input = random.randint(1, 10)
            if i == n:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
        print(matrix[i])
else:
    print("One does not simply create a identity matrix without a square matrix.")

