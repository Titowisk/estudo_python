frase = input("Digite uma frase: ")

frase_sem_espaco = ""

for letra in frase:
    if letra != " ":
        frase_sem_espaco += letra


if frase_sem_espaco == frase_sem_espaco[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase é normal.")