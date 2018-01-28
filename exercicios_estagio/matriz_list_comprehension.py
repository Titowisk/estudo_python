# code:utf-8

# Matrix criada com Compreensão de lista.

def print_matrix(matriz):
    for linha in matriz:
        print(linha)

import random

matriz_lc = [[random.randint(0, 9) for y in range (0, 6)] for x in range(0, random.randint(1, 5))]

print("")
print_matrix(matriz_lc)