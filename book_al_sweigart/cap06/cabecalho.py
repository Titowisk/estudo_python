#! python
# cabecalho.py - Um programa que facilita o preenchimento de cabecalho

INFO = {
    'nome': 'Vitor',
    'sobrenome': 'Rabelo Filardi Ribeiro',
    'CEP': '40270010',
}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Como usar:')
    print('Ele abre o python e digita: cabecalho.py [titulo]')
    print('Isso copia o titulo pedido: nome, sobrenome ou CEP')
    sys.exit()

titulo = sys.arg[1]

if titulo in INFO:
    pyperclip.copy(INFO[titulo])
    print('A informação sobre {} foi copiada'.format(titulo))
else:
    print('Não há info sobre {}'.format(titulo))
