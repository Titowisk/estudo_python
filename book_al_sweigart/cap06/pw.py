#! python
#coding = utf-8
# pw.py - Um programa para repositório de senha que não é seguro.

PASSWORDS = {
    'email': 'Fgu76%$89_iUolOP7s627a*&SH&P*SH&SS&*',
    'blog': 'VAj76hji7hjjh5J38SDJFKi*9OLJ',
    'luggage': '12345'
}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   #O primeiro argumento da linha de comando é o nome da conta.

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for {} copied to clipboard'.format(account))
else:
    print('There is no account name {}'.format(account))
