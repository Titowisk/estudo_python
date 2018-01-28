# coding=utf-8

array = []
array_dobro = []

for i in range(10):
    array.append(int(input("Entre com o elemento {} do vetor: ".format(i))))
    array_dobro.append(array[i]*2)

for j in range(10):    
    print("Vetor: {} -- Vetor em dobro: {}".format(array[j], array_dobro[j]))