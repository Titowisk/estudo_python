# coding=utf-8
#Author: Vito Ribeiro

# This program is for searching e-mails and phone numbers (Brazil) and return
# what is found.

# Common Mobile Phonenumber from Brazil:  55 (71) 9 9956-5726
# Common Phonenumber from Brazil: 55 (71) 3382-9364
# Common e-mail: something@something.com.br

import pyperclip
import re

# 1 Copy the text from any source.

# 2 Use Regex to search through it.

# 3 Return the e-mails and phone numbers accordingly

text = pyperclip.paste()

phoneRegex = re.compile(r'''(       # (71) 3382-9364
    (0?\d{2}|\(0?\d{2}\))?            # (71) (opcional)
    (\s|-|\.|_)?                    # separador
    \d{4}                           # 3382
    (\s|-|\.|_)                     # separador
    \d{4}                           # 3382
)''', re.VERBOSE)

mobilePhoneRegex = re.compile(r'''( # (71) 99956-5726
    (0?\d{2}|\(0?\d{2}\))?          # (71)
    (\s|-|\.|_)                     # separador (opcional)
    (9\s?)                          # digito 9 adicional
    \d{4}                           # 4 digitos
    (\s|-|\.|_)                     # separador
    \d{4}
)''', re.VERBOSE)

emailRegex = re.compile(r'\S+@\S+\.com\S*') # (anything except breaklines, spaces)@("").com(any characteres)

# .findall() retorna uma lista de tuplas: [(group 0), (group 1), group(2), ...]
# group 0 retorna o resultado total.

emails = emailRegex.findall(text)

phone_numbers = phoneRegex.findall(text)

mobile_phone_numbers = mobilePhoneRegex.findall(text)

if emails:
    for grupo in emails:
        print(grupo)

if phone_numbers:
    for grupo in phone_numbers:
        print(grupo[0])
else:
    print('Erro em phoneRegex')

if mobile_phone_numbers:
    for grupo in mobile_phone_numbers:
        print(grupo[0])
else:
    print('Erro em mobilePhoneRegex')
