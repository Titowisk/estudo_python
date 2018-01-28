# coding=utf-8

# Salada de Frutas


list = ['apples', 'bananas', 'tofu', 'cats']

def lista_para_texto(list):

    for indice in range(0, len(list)):
        if indice == len(list)-1:
            print('and {}'.format(list[-1]))
        else:
            print(list[indice], end=', ')



if __name__ == '__main__':
    lista_para_texto(list)