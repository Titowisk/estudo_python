# coding=utf-8

# coding=utf-8
#Author: Vito Ribeiro

# This program is for searching e-mails and phone numbers (Brazil) and return
# what is found.

# Common Mobile Phonenumber from Brazil:  55 (71) 9 9956-5726
# Common Phonenumber from Brazil: 55 (71) 3382-9364
# Common e-mail: something@something.com.br

#Now functions based.

import re, pyperclip



def mobile_phone_searcher(clipboard_text):
    mobilePhoneRegex = re.compile(r'''( # (71) 99956-5726
        (0?\d{2}|\(0?\d{2}\))?          # (71)
        (\s|-|\.|_)                     # separador (opcional)
        (9\s?)                          # digito 9 adicional
        \d{4}                           # 4 digitos
        (\s|-|\.|_)                     # separador
        \d{4}
    )''', re.VERBOSE)

    mobile_phone_numbers = mobilePhoneRegex.findall(clipboard_text)

    if mobile_phone_numbers:
        for grupo in mobile_phone_numbers:
            print(grupo[0])
    else:
        print('Erro em mobile_phone_searcher')

def phone_searcher(clipboard_text):

    phoneRegex = re.compile(r'''(       # (71) 3382-9364
        (0?\d{2}|\(0?\d{2}\))?          # (71) (opcional)
        (\s|-|\.|_)?                    # separador
        \d{4}                           # 3382
        (\s|-|\.|_)                     # separador
        \d{4}                           # 3382
    )''', re.VERBOSE)

    phone_numbers = phoneRegex.findall(clipboard_text)
    if phone_numbers:
        for grupo in phone_numbers:
            print(grupo[0])
    else:
        print('Erro em phone_searcher')

def email_searcher(clipboard_text):
    emailRegex = re.compile(r'\S+@\S+\.com\S*')

    emails = emailRegex.findall(clipboard_text)

    if emails:
        for grupo in emails:
            print(grupo)
    else:
        print("Erro em email_searcher.")

def all_searcher(clipboard_text):
    pass

def search_options(clipboard_text):
    welcome = '''
        Para utilizar este programa, é necessário que você copie o texto desejado
utilizando ctrl+c e depois digitar a opção deseja.
    '''
    msg = '''Digite:
                1 para procurar por emails;
                2 para procurar por números de telefone;
                3 para procurar por números de celular.
'''
    print(welcome)
    print(msg)
    numero = int(input())
    if numero == 1:
        email_searcher(clipboard_text)
    elif numero == 2:
        phone_searcher(clipboard_text)
    elif numero == 3:
        mobile_phone_searcher(clipboard_text)
    else:
        print('Você precisa digitar uma das seguintes opções:', msg)


text = pyperclip.paste()
search_options(text)
