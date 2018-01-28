"""
1) Descubro o primeiro número que torna a sequência, não crescente
2) Removo o elemento e analiso se a sequência resultante é crescente
    a - Se for, então é possivel tirar 1 elemento...
    b - caso contrário não é possivel
"""
sequence = [1, 3, 2]

def first_bad_pair(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i  
    return -1



j = first_bad_pair(sequence)
if j == -1:
    ais = True
new_seq = sequence[:j] + sequence[j+1:]
if first_bad_pair(new_seq) == -1:
    ais = True
new_seq = sequence[:j+1] + sequence[j+2:]
if first_bad_pair(new_seq) == -1:
    ais = True
ais = False

