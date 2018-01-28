# o primeiro elemento não nulo tem que ser 1
# todos os numeros abaixo desse elemento terão que ser nulos
# se tiver uma linha nula, todas as outras linhas abaixo terao que ser tb


# Pra classificar em escada tem que iterar a matriz toda
# mas basta uma condição errada para classificar como não-escada
matriz =[[0, 2, 1],
         [1, 0, -3],
         [0, 0, 0]]

escada = True
linha = len(matriz)
coluna = len(matriz[0])
while escada:
    #verificar linhas nulas
    for i in range(linha): # 0 <= i <= linha-1
        linha_nula = [0]*linha
        if ( matriz[i] == linha_nula) and (i != linha-1):
            if matriz[i+1] == linha_nula:
                continue
            else:
                escada = False
        # iterar sobre cada coluna da linha i
        for j in range(coluna): # 0 <= j <= coluna-1
            if matriz[i][j] == 0:
                continue
            elif matriz[i][j] == 1:
                # verificar algarismos abaixo
                for f in range(i+1, linha): # i+1 <= f <= linha-1
                    if matriz[f][j] == 0:
                        continue
                    else: # se um algarismo != 0 for encontrado, para.
                        escada = False
                # fim da verificação, pode ir pra proxima linha
                break # vai para a proxima linha
            else: # o primeiro algarismo não nulo diferente de 1
                escada = False
    else: # se chegar até aqui sem quebrar o loop while, então escada=True
        break

if escada:
    print("A matriz é escada")
else:
    print("A matriz NÃO é escada")