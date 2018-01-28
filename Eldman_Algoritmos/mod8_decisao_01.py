# coding=utf-8

print("Digite o primeiro número: ")
n1 = int(input())
print("Digite o número divisor: ")
n2 = int(input())

if n1 % n2 == 0:
    print("{} é divisível por {}".format(n1, n2))
else:
    print("%d não é divisível por %d" % (n1, n2))