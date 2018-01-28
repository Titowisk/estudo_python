# code=utf-8
# path: c:\Users\Tito\Documents\programinhas_python\exercicios_estagio\matriz_escada.py

#Uma matriz escada atende a certos requisitos:
#   1) o primeiro elemento não nulo da linha é 1;
#   2) cada coluna que contém o primeiro elemento não nulo de uma linha tem todos os seus outros
#   elementos iguais a 0;
#   3) toda linha nula ocorre abaixo de todas as linhas não nulas


# Como fazer?
# Percorrer a matriz com loops for
# a - verifica se na linha tem 0 ou 1
# matriz 3x4
matriz = [[1, 0, 2],
          [0, 0, 0],
          [0, -1, 2]]

linha = len(matriz)
coluna = len(matriz[0])

escada = True

for i in range(linha):
    # verifica linhas nulas
    lista_nula = [0] * coluna
    if matriz[i] == lista_nula:
        if i < linha-1: 
            if matriz[i+1] == lista_nula:
                continue
        else:
            escada = False
    # verificação do primeiro algarismo não-nulo
    for j in range(coluna): # ixj
        if matriz[i][j] == 0: 
            continue
        elif matriz[i][j] == 1: # 1x4 ->
            # verifica se na coluna os algarismos abaixo são 0  
            for p in range(i+1, linha): # -> 2x4 ==0 , 3x4 == 0, 4x4 ==0
                if p == (linha):
                    break
                elif matriz[p][j] == 0:
                    continue
                else:
                    escada = False
            else:
                break
        else:
            escada = False
 

if not escada:
    print("A matriz não é Escada.")
else:
    print("A matriz é escada.")

# -------------------------------------------------------------------------------------------------------

