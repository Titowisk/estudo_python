# Primeiro ler o inteiro N
# Criar a Lista
# Ler inputs do usuario até que o numero de inputs ultrapasse o inteiro N

N = int(input())
list = []
i = 1
while i <= N:
    entry = input().split()
    command = entry[0]
    if command == 'insert':
        list.insert(int(entry[1]), int(entry[2]))
    elif command == 'print':
        print(list)
    elif command == 'remove':
        list.remove(int(entry[1]))
    elif command == 'append':
        list.append(int(entry[1]))
    elif command == 'sort':
        list.sort()
    elif command == 'pop':
        list.pop()
    elif command == 'reverse':
        list.reverse()
    i+=1