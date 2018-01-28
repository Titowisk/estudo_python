#coding=utf-8

import random

def gerar_mega2():
    sorteio = []
    while len(sorteio) <=5:
        d = random.randint(1, 60)
        if d in sorteio:
            continue
        else:
            sorteio.append(d)
    sorteio.sort()
    return sorteio

sorteio = gerar_mega2()
n_apostas = 0
ganhador = False
while ganhador == False:
    numero_sorteado = gerar_mega2()
    if numero_sorteado != sorteio:
        n_apostas +=1
        if n_apostas == 100:
            print('Você já fez {} apostas'.format(n_apostas))
        continue
    else:
        ganhador = True

print(n_apostas)
