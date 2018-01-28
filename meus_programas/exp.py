# -*- coding: utf-8 -*-
# Jogo da adivinhação
import random
print('----------------------------------')
print('Bem-vindo ao jogo da Adivinhação!')
print('----------------------------------')

numero_secreto = random.randrange(0, 101)

numero_de_tentativas = 3
rodada = 1


#while(rodada <= numero_de_tentativas):
for rodada in range(1, numero_de_tentativas+1):
    print('Rodada {} de {}.'.format(rodada, numero_de_tentativas))
    chute = int(input('Digite seu palpite (o número deve estar entre 1 e 100): '))

    while (chute < 1 or chute > 100):
        print('Por favor, digite um número entre 1 a 100.')
        chute = int(input('Digite seu palpite (o número deve estar entre 1 e 100): '))


    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto
    if(acertou):
        print('Você acertou!')
        break
    elif(menor):
        print('Errou! Seu palpite foi menor que o número secreto.')
    elif(maior):
        print('Errou! Seu palpite foi maior que o número secreto.')
#    rodada += 1

print('O número era {}. Mais sorte na próxima ;)'.format(numero_secreto))
print('Fim do jogo.')
print('--------------------------------------------------------------')
