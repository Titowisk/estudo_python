# manual .strip() function

prhase = input("Type a phrase: ")

word = ""
words_list = []
for character in prhase:
    if character != " ":
        word += character
    else:
        words_list.append(word)
        word = ""
else:
    words_list.append(word)
    word = ""

print(words_list)