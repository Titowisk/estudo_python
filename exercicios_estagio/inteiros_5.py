# 5) Loja de Discos
import random

vendas_disco = {}

for x in range(1, 32):
    y = random.randint(1, 40)
    vendas_disco[x] = y

maior_quant = vendas_disco[1]
for a, b in vendas_disco.items():
    print(a," ", b)
    if b >= maior_quant:
        maior_quant = b
        dia = a
    else:
        continue

print("A maior quantidade de discos vendidos é {} \ne ocorre no dia {}".format(maior_quant, dia))
        