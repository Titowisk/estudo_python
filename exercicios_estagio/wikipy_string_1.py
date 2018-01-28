# Tamanho de strings. Faça um programa que leia 2 strings 
# e informe o conteúdo delas seguido do seu comprimento. 
# Informe também se as duas strings possuem o mesmo comprimento 
# e são iguais ou diferentes no conteúdo.

frase1 = input("Digite uma frase: ")
frase2 = input("Digite outra frase: ")

comp1 = len(frase1)
comp2 = len(frase2)

print("String 1: {}".format(frase1))
print("String 2: {}".format(frase2))

print("Tamanho de '{0}': {1}".format(frase1, comp1))
print("Tamanho de '{0}': {1}".format(frase2, comp2))

if frase1 == frase2:
    msg = "As duas frases são iguais."
else:
    msg = "As duas frases são diferentes."
print(msg)
print("Fim")