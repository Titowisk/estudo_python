# coins = [10, 4, 3, 2]
valor = 15

def coin_change(valor):
    for q10 in range(2):
        for q4 in range(2):
            for q3 in range(2):
                for q2 in range(2):
                    if (q10*10 + q4*4 + q3*3 + q2*2) == valor:
                        return print("É possivel pagar exatamente")
    return print("Não é possível pagar exatamente.")

coin_change(valor)
