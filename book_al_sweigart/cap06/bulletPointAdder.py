#! python
#coding=utf-8
# bulletPointerAdder.py - Um programa que adiciona '*' (asterisco) no começo de cada frase
#na área de transferência.


import pyperclip

#Primeiro captura o texto copiado.
copiado = pyperclip.paste()

#Realiza-se os procedimentos para colocar o asterisco.
lista = copiado.split('\r\n')

lista_com_asterisco = []

for i in lista:
    novo_i = i.rjust(len(i)+1, '*')
    lista_com_asterisco.append(novo_i)

lista_pronta = '\n'.join(lista_com_asterisco)

#Devolve para a área de transferência a mesma lista.

pyperclip.copy(lista_pronta)
