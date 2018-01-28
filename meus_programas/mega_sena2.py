# coding: utf-8

import random

sorteio = []

def gerar_mega2():
    while len(sorteio) <=5:
        d = random.randint(1, 60)
        if d in sorteio:
            continue
        else:
            sorteio.append(d)
    sorteio.sort()
    return sorteio
