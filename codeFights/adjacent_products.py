
inputArray = [3, 6, -2, -5, 7, 3]

maior_produto = inputArray[0]*inputArray[1]
for x in range(1, len(inputArray)):
    produto = inputArray[x-1] * inputArray[x]
    if produto <= maior_produto:
        continue
    else:
        maior_produto = produto