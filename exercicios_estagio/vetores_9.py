# coding=utf-8

#9.  Dadas duas seqüências com n números inteiros entre 0 e 9,
#  interpretadas como dois números inteiros de n algarismos, 
# calcular a seqüência de números que representa a soma dos dois inteiros.
# 82434251
# 33752337
#116186588

#        8    2    4    3    4    2    5    1
# +      3    3    7    5    2    3    3    7
# = 1    1    6    1    8    6    5    8    8

import sys

usage = "python vetores_9.py [number1] [number2]"

# Capturar os numeros em forma de string para a soma

if len(sys.argv) < 3 or sys.argv[1] in {'-h', '--help'}:
    print(usage)
else:
    number1 = '0' + sys.argv[1]
    number2= '0' + sys.argv[2]



#ver qual numero dado é o maior
number_len_diff = abs(len(number1)-len(number2))
if number1 > number2:
    greater = number1
    number2 = '0'*number_len_diff + number2
elif number2 > number1:
    greater = number2
    number1 = '0'*number_len_diff + number1
else:
    greater = number2


# iterar sobre os numeros, de trás pra frente
# somar algarismo por algarismo:
#   se a soma for mais que 10 adiciona 1 na próxima soma
#   a primeira soma jamais terá 1 adicionado
a = -1
bonus = 0
result_list = []
last_sum = abs(a) == len(greater)
while abs(a) <= len(greater): # -len(greater) < a < -1 
    sum = int(number1[a]) + int(number2[a]) 
    if sum > 9:
        rest = sum - 10
        result_list.insert(0, rest+bonus)
        bonus = 1
        
    else:
        if sum+bonus == 10:
            result_list.insert(0, 0)
            bonus = 1
        else:
            result_list.insert(0, sum+bonus)
            bonus = 0

    if last_sum and bonus == 1:
        result_list.insert(0, bonus)

    a -= 1

# Imprimir a soma de forma organizada

for l in number1:
    print(l, end=" ")
print(" ")
print("+")

for l in number2:
    print(l, end=" ")

print(" ")
print("-"*(2*len(number2)-1))

for n in result_list:
    print(n, end=" ")
