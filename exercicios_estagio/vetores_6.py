# coding=utf-8
# 6.  (COMP 89) Dados dois strings (um contendo uma frase e outro contendo uma palavra), 
# determine o número de vezes que a palavra ocorre na frase.

frase = "ANA E MARIANA GOSTAM DE BANANA"
word = 'ANA'
word_count = 0
loop_limit = len(frase) + 1 - len(word)

for letra in range(loop_limit):
    if frase[letra:letra+len(word)] == word:
        word_count += 1

print(word_count)