"""
Para cada elemento da lista:
    1- copia a sequencia dada;
    2 - retira o elemento;
    3 - Verifica se a nova sequencia é crescente
        a - verifica se cada valor é maior que o seu antecessor;
        b - cada vez que for adiciona True em uma lista ou False quando não for;
        c - Se não houver False na lista booleana criada retorna True

"""
sequence = [1, 3, 2]
answearList = []
ais = False
for x in range(len(sequence)):                      
    s_copy = sequence.copy()
    s_copy.pop(x)
    answearList.append([])
    for y in range(1, len(s_copy)):
        if s_copy[y] > s_copy[y-1]:
            answearList[x].append(True)
        else:
            answearList[x].append(False)
    else:    
        if answearList[x].count(False) == 0:
                ais = True
                break 
            
"""
for a in answearList:
    if a.count(False) == 0:
        ais = True
        break
    else:
        continue
"""

# Diz que demorou de mais para realizar a tarefa.
"""
def almostIncreasingSequence(sequence):

    answearList = []
    ais = False
    for x in range(len(sequence)):                      
        s_copy = sequence.copy()
        s_copy.pop(x)
        answearList.append([])
        for y in range(1, len(s_copy)):
            if s_copy[y] > s_copy[y-1]:
                answearList[x].append(True)
            else:
                answearList[x].append(False)
        else:    
            if answearList[x].count(False) == 0:
                    ais = True
                    break 
    return ais
"""