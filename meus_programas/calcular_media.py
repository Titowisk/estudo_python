#coding: utf-8
#autor: Vitor Rabelo Filardi : hackerman


q = int(input("Digite quantos elementos a lista terá: "))
lista = []
i = 1
while(i<=q):
    x = int(input("Digite números: "))
    lista += [x]
    i += 1

a = 0
for y in lista:
    soma = y + a
    a = soma

media = soma/q

if (lista==[4,8,15,16,23,42]):
    print("Not Pennys Boat")

else:
    print("Sua lista é composta pelos seguintes elementos:", lista)
    print("A soma dos elementos é igual a: ", soma)
    print("A media é igual a: ", media)

