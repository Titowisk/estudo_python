# coding=utf-8


msg = input("Digite a mensagem: ")
cripto_msg = ""

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"
, "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w"
, "x", "y", "z"]

#criptography i+2

for character in msg:
    lower_char = character.lower()
    if character == " ":
            cripto_msg += "77"
    for i in range(len(abc)):
        if lower_char == abc[i]:
            if i+2 < 10:
                cripto_msg += "0" + str(i+2)
            else:
                cripto_msg += str(i+2)  
else:
    cripto_msg += "."

print(cripto_msg)

# de-criptography 
decripto_msg = ""
for i in range(0, len(cripto_msg)-2, 2):
    for n in range(len(abc)):
        if int(cripto_msg[i:i+2])-2 == n: # "20" == 'a'
            decripto_msg += abc[n]
        elif cripto_msg[i:i+2] == "77": 
            decripto_msg += " "
            break
else:
    decripto_msg += "."

print(decripto_msg)
