# coding=utf-8

import sys

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

One = [" * ",
       "** ",
       " * ",
       " * ",
       " * ",
       " * ",
       "***"]

Two = [" *** ",
       "*   *",
       "*  * ",
       "  *  ",
       " *   ",
       "*    ",
       "*****"]

Three = [" *** ",
         "*   *",
         "    *",
         "  ** ",
         "    *",
         "*   *",
         " *** "]
Four  = ["    * ",
         "   ** ",
         "  * * ",
         " *  * ",
         "******",
         "    * ",
         "    * "]
Five  = ["*****",
         "*    ",
         "*    ",
         " *** ",
         "    *",
         "*   *",
         " *** "]
Six   = [" *** ",
         "*   *",
         "*    ",
         "**** ",
         "*   *",
         "*   *",
         " *** "]
Seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]
Eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]
Nine  = [" ****",
         "*   *",
         "*   *",
         " ****",
         "    *",
         "    *",
         " *** "]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1] # '4789145'
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])   # 4
            digit = Digits[number]         # 4 -> Four
            line += digit[row] + " "       # Cria uma string "" com a primeira linha de Four + " "
            column += 1                    # Prossegue para a próxima linha do próximo dígito.
        print(line)                        # Quando a primeira linha de numeros está toda formada, imprime a linha completa.
        row += 1                           # Prossegue para a segunda linha e assim em diante
except IndexError:
    print('usage: bigdigits.py <number>')
except ValueError as err:
    print("{} in {}".format(err, digits))
