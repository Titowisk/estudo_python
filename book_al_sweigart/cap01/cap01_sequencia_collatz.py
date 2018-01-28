# coding=utf-8

def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    return number
try:
    print('Sequência Collatz')
    number = int(input('Digite um número: '))
except ValueError:
    print('Por favor digite um número inteiro.')
    number = int(input('Digite um número: '))


while number != 1:
    number = collatz(number)
    print(number)


if __name__ == '__main__':
    collatz(number)

