# coding=utf-8

import random

sorteio = set()

def gerar_mega():
    while len(sorteio) <= 5:
        d = random.randint(1, 60)
        sorteio.add(d)
    print(sorted(sorteio))

gerar_mega()