# 7.Conta espaços e vogais. 
# Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), 
# conte:
#   quantos espaços em branco existem na frase.
#   quantas vezes aparecem as vogais a, e, i, o, u.

frase = input("Digite uma frase: ").lower()

espacos_brancos = frase.count(" ")
vogal_a = frase.count("a")
vogal_e = frase.count("e")
vogal_i = frase.count("i")
vogal_o = frase.count("o")
vogal_u = frase.count("u")

print("Espaços em branco: {} espaços.".format(espacos_brancos))
print("Vogal 'a' aparece {} vezes.".format(vogal_a))
print("Vogal 'e' aparece {} vezes.".format(vogal_e))
print("Vogal 'i' aparece {} vezes.".format(vogal_i))
print("Vogal 'o' aparece {} vezes.".format(vogal_o))
print("Vogal 'u' aparece {} vezes.".format(vogal_u))