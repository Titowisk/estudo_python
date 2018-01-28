# ime.usp exercicios
import random

# 1) 
lista_inteiros = list(range(8))

for i in lista_inteiros:
    print("{} - {}".format(i, i**2))

# 2)

n = random.randint(1, 10)
soma = 0

for i in range(n):
    soma = soma + i
print("n = {} e a soma dos {} primeiros números = {}".format(n, n, soma))
