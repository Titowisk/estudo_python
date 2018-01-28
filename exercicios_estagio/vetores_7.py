# coding=utf-8

#7.  (MAT 88) Dada uma seqüência de n números reais, 
# determinar os números que compõem a seqüência 
# e o número de vezes que cada um deles ocorre na mesma.

# Exemplo: n = 8
# Seqüência: -1.7,  3.0,  0.0,  1.5,  0.0, -1.7,  2.3, -1,7

sequence = [-1.7,  3.0,  0.0,  1.5,  0.0, -1.7,  2.3, -1.7]

ocurrences = {}

for x in sequence:
    if x not in ocurrences.keys():
        ocurrences[x] = 1
    else:
        ocurrences[x] += 1

for k,v in ocurrences.items():
    print("{} appears {} times in the list.".format(k, v))