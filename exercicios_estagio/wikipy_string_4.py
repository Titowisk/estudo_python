# 4. Nome na vertical em escada.
# Modifique o programa anterior de forma a mostrar o nome em formato de escada.

nome = input("Digite seu nome: ").upper()

for letra in range(1, len(nome)+1):
    print(nome[0:letra])

# 5. Nome na vertical em escada invertida. 
# Altere o programa anterior de modo que a escada seja invertida.

for letra in range(len(nome)+1, 0, -1):
    print(nome[0:letra])
