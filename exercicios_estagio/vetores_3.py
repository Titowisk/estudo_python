# coding=utf-8

# 3.  Tentando descobrir se um dado era viciado, 
# um dono de cassino honesto (ha! ha! ha! ha!) o lançou n vezes. 
# Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face. 
import random

list_results = []
dice_faces = [1, 2, 3, 4, 5, 6]
ocurrences = [0, 0, 0, 0, 0, 0]
n = random.randint(30, 90)

# generates random dice results
for x in range(n):
    list_results.append(random.randint(1, 7))

# number of each ocurrences
for r in range(len(list_results)):
    for face in range(len(dice_faces)):
        if list_results[r] == dice_faces[face]:
            ocurrences[face] += 1

print("-"*20)
print("Lista de resultados:")
print(list_results)
print("Lista de faces do dado:")
print(dice_faces)
print("Lista de ocorrências respectivas:")
print(ocurrences)
