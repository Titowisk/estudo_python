# coding=utf-8

def primo(numero):
    i = 2
    p = 1
    if numero == 1: # se numero for 1, numero é primo
        p = 1
    else:
        while i < numero:
            if numero % i == 0:
                p = 0 # numero não é primo
                break
            i += 1 
            if i == numero:
                p = 1
    return p    

n = int(input())
soma = 0
for numero in range(n+1):
    if primo(numero) == 1:
        soma = soma + numero
    else:
        continue
print("A soma dos numero que são primos até {} é: {}".format(n, soma))