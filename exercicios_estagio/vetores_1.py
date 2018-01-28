# coding:utf-8

"""
1.  Dada uma seqüência de n números, imprimi-la na ordem inversa à da leitura. 
"""

lista = [1, 2, 3, 4, 5]

for x in range(1, len(lista)+1):
    print(lista[-x])

lista_reversa = lista[::-1]
print(lista_reversa)
