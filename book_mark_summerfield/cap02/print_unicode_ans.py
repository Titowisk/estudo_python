import sys, unicodedata

def print_unicode_table(word):
    print("decimal  hex  chr  {0:^40}".format("name"))
    print("-------  ---  ---  {0:-<40}".format(""))

    code = ord(" ")
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        if word is None or word in name.lower():
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(code, name.title()))

        code += 1

word = None
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string1 string2 string3 ...]".format(sys.argv[0]))
        print("Example: ")
        print("    python {} greek symbol".format(sys.argv[0]))
        print("    Returns all unicodes that have 'greek symbol' in their names ")
        word = 0
    else:
       word = " ".join(sys.argv[1:])
       word = word.lower()
if word != 0:
    print_unicode_table(word)