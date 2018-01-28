# ordenar uma lista qualquer
import random

lista = list(range(random.randint(1, 10)))
random.shuffle(lista)
print(lista)
print("")
lista_ordenada = []

while len(lista) > 0:
    menor = lista[0]                    
    for x in range(len(lista)):                 
        if lista[x] <= menor:             
            menor = lista[x]
    lista_ordenada.append(menor) 
    lista.remove(menor)                 

print(lista_ordenada)
