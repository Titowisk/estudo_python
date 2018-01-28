def letterCounter(inputString):
    letter_quantity = dict()
    for l in inputString:
        if l not in letter_quantity:
            letter_quantity.setdefault(l, 1)
        else:
            letter_quantity[l] += 1
    
    return letter_quantity


def palindromeRearranging(inputString):
# if len(string) is even, then the quantity of each letter must be even
# if len(string) is odd, only one letter can have a odd quantity
    palindrome = True
    if len(inputString) % 2 == 0: # if even
        for v in letterCounter(inputString).values():
            if v % 2 != 0:
                palindrome = False
                break
        
    else: # if odd
        only_one_letter = 0
        for v in letterCounter(inputString).values():
            if v % 2 != 0:
                only_one_letter += 1
                if only_one_letter > 2:
                    palindrome = False
                    break
                    
    return palindrome