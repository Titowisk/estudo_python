#coding = utf-8

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

def printTable():
    pass

colWidths = [0] * len(tableData)

def maior_palavra(lista_de_palavras):
    max = ''
    for i in lista_de_palavras:
        if len(i) > len(max):
            max = i
    return len(max)


for x in range(len(tableData)):
    colWidths[x] = maior_palavra(tableData[x])  #[8, 5, 5]  colWidths[0] = 8

tabela_ajustada = []

for x in range(len(tableData[x])):         #0,1,2,3
    for y in range(len(tableData)):  #0,1,2
        if y == len(tableData)-1:
            print(tableData[y][x].rjust(colWidths[y]))
        else:
            print(tableData[y][x].rjust(colWidths[y]), end='  fuck this shit  ')
