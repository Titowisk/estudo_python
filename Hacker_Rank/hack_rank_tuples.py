# Ler um inteiro n
# ler n inteiros separados por espaços
# formar uma tupla com os n inteiros separados

n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))