try:
    n1 = int(input("Digite um número inteiro: "))
    if n1 % 2 ==0 and n1 % 3 == 0:
        print("Ok")
    else:
        print("NOT ok")
except ValueError:
    print("Você deve digitar um número inteiro.")





