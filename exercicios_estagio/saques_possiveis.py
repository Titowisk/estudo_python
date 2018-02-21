"""
EX:

Valor do saque: 22
 6    8     4       7     10     20 -> quantidades
N2    N5   N10     N20    N50    N100 -> cédulas
"""
# 2 + 20
# 2 + 10 + 10
# 2 + 10 + 5 + 5
# 2 + 5 + 5 + 5 + 5
# 2 + 5x2 + 10
# 2 + 5x2 + 5 + 5
saque = 22
q2, q5, q10, q20 = 6, 8, 4, 7 
formas_possiveis = 0
for q2 in range(q2+1):
    for q5 in range(q5+1):
        for q10 in range(q10+1):
            for q20 in range(q20+1):
                if (2*q2 + 5*q5 + 10*q10 + 20*q20) == saque:
                    formas_possiveis += 1
print(formas_possiveis)