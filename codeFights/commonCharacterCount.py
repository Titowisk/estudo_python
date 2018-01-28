s1 = "aabcc"
s2 = "adcaa"

already_checked = []
common_char = 0
for character in s1:
    if character in already_checked:
        continue
    elif character in s2:
        already_checked.append(character)
        c2 = s2.count(character)
        c1 = s1.count(character)
        if c2 <= c1:
            common_char += c2
        else:
            common_char += c1
    else:
        continue
       
print(common_char)

# best Answear
# def commonCharacterCount(s1, s2):
#   return sum(min(s1.count(x), s2.count(x)) for x in set(s1))