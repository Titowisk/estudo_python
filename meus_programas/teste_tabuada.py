#coding utf-8

def tabuada(x):
    i = 0
    while(i<=10):
        total = x * i
        print(x, "x", i, "=", total)
        i+=1


x = int(input('Deseja obter a tabuada para qual número? '))

tabuada(x)