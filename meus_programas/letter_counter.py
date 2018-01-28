
def letterCounter(inputString):
    letter_quantity = dict()
    for l in inputString:
        if l not in letter_quantity:
            letter_quantity.setdefault(l, 1)
        else:
            letter_quantity[l] += 1
    
    return letter_quantity

answear = letterCounter('titowisk')
print(answear)

for k in answear:
    print(answear[k])