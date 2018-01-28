letra = input("Digite uma letra: ")
letra_m = letra.lower()

vogais = ['a', 'e', 'i', 'o', 'u']

if letra_m in vogais:
    print("{} é uma vogal".format(letra_m))
else:
    print("{} é uma consoante".format(letra_m))