#! python
#coding = utf-8
# pw.py - Um programa para repositório de senha que não é seguro.

LORE_IPSIUM = {
    'lore1': 'Fgu76%$89_iUolOP7s627a*&SH&P*SH&SS&*',
    'lore2': 'VAj76hji7hjjh5J38SDJFKi*9OLJ',
    'lore3': '12345'
}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [lp] - copy lp paragraph')
    sys.exit()

lp = sys.argv[1]   #O primeiro argumento da linha de comando é o nome da conta.

if lp in LORE_IPSIUM:
    pyperclip.copy(LORE_IPSIUM[lp])
    print('Paragrafo copiado para área de transferência'
else:
    print('Só tem lp1, lp2 e lp3')

# Para executar digite lore lpx na janela de comando.
