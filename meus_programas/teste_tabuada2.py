# coding=utf-8

def tabuada(chosen_number):
    i = 0
    while i != 10:
        total = chosen_number * i
        print("{0} vezes {1} = {2}".format(chosen_number, i, total))
        i += 1

def main():
    user_text = "Digite o algarismo para obter sua taboada: "
    try:
        chosen_number = int(input(user_text))
        print("Tabuada de {0}".format(chosen_number))
        tabuada(chosen_number)
    except ValueError as err:
        print("Você precisa digitar um número inteiro válido.")

main()