# coding=utf-8

"""
2.  Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. 
A prova consta de 30 questões, cada uma com cinco alternativas identificadas por 
A, B, C, D e E. Para isso são dados:

    o cartão gabarito;
    o número de alunos da turma;
    o cartão de respostas para cada aluno, contendo o seu número e suas respostas.
"""
import random

alternativas = ['A', 'B', 'C', 'D', 'E']
gabarito = []
prova = []
alunos = ['João', 'Cris', 'Raquel', 'Maria']
acertos = []


# Gera um gabarito aleatório
for q in range(30):
    gabarito.append(random.choice(alternativas))

# gera provas aleatórias para cada aluno
for a in range(len(alunos)):
    prova.append([])
    for q in range(1, 31):
        prova[a].append(random.choice(alternativas))

#Corrigi as provas de cada aluno
for a in range(len(alunos)):
    acertos.append(0)
    for q in range(30):
        if prova[a][q] == gabarito[q]:
            acertos[a] += 1

# o cartão gabarito;
print("Gabarito da Prova:")
print(">      {}".format(gabarito))
print("-"*90)

# o cartão de respostas para cada aluno, contendo o seu número e suas respostas.
for a in range(len(alunos)):
    print("Aluno(a): {}".format(alunos[a]))
    print("Prova: {}".format(prova[a]))
    print("Acertos: {}".format(acertos[a]))
    print("-------------------------------")
    print("-------------------------------")

# Resumo:
print("Resumo:")
print(alunos)
print(acertos)