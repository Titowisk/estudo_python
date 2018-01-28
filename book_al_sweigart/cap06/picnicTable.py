# coding=utf-8

def printPicnic(itemsDict, leftWidth, rigthWidth):
    print('PICNIC ITEMS'.center(leftWidth + rigthWidth, '-'))
    for k, v in itemsDict.items():
        print(k. ljust(leftWidth, '.') + str(v).rjust(rigthWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
print(' ')
printPicnic(picnicItems, 20, 6)
