# coding=utf-8

# a)
def contaDigitos(n, d):
    lista_s = str(n)
    digito = str(d)

    contador = 0
    for i in lista_s:
        if digito == i:
            contador += 1
        else:
            continue
    return "O digito {} aparece {} vezes em {}".format(d, contador, n)

# b)

