# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres,
# mostre−a e diga se é um palíndromo ou não.

frase = input("Digite uma frase: ")

lista_frase = frase.split()

string_sem_espaco = "".join(lista_frase)

if string_sem_espaco == string_sem_espaco[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase é normal.")