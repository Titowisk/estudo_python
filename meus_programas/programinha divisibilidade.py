#coding utf-8

#Verificar divisibilidade entre dois números.


num1 = int(input("Digite aqui um número: "))
num2 = int(input("Digite aqui um divisor: "))

if(num1 % num2==0):
    print("%i é divisível por %i"%(num1,num2))
else:
    print("%i não é divisível por %i"%(num1,num2))
