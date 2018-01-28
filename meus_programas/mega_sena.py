# coding=utf-8
#Aplicativo de apostas na mega sena.
# Autor: Vitor RFR

import random
def gerar_mega():
    dezenas = []

    #Irá gerar as 6 dezenas da mega sena.
    for a in range(6):
        x = random.randrange(1, 61)  #irá gerar números aleatórios inteiros de 1 a 60.
        dezenas.append(x)

    # Irá verificar as 6 dezenas da mega sena para evitar repetições.
    verificador = True
    while verificador == True:
        if dezenas[0] == dezenas[1] or dezenas[0] == dezenas[2] or dezenas[0] == dezenas[3] or dezenas[0] == dezenas[4] or dezenas[0] == dezenas[5]:
            verificador = False

        elif dezenas[1] == dezenas[2] or dezenas[1] == dezenas[3] or dezenas[1] == dezenas[4] or dezenas[1] == dezenas[5]:
            verificador = False

        elif dezenas[2] == dezenas[3] or dezenas[2] == dezenas[4] or dezenas[2] == dezenas[5]:
            verificador = False

        elif dezenas[3] == dezenas[4] or dezenas[3] == dezenas[5]:
            verificador = False

        elif dezenas[4] == dezenas[5]:
            verificador = False

        else:
            break
    #Se tiver dezena igual, verificador será igual a False.
    if verificador == False:
        gerar_mega()
    else:
        print('-'*48)
        print('-'*11, sorted(dezenas), '-'*11)
        print('-'*48)

if __name__ == '__main__':
    gerar_mega()
