theBoard = {
'top-L': '', 'top-M': '', 'top-R': '',
'mid-L': '', 'mid-M': '', 'mid-R': '',
'low-L': '', 'low-M': '', 'low-R': ''
}

for k in theBoard.keys():
    theBoard[k] = ' '

def printBoard(board):
    print('{}|{}|{}'.format(board['top-L'], board['top-M'], board['top-R']))
    print('-+-+-')
    print('{}|{}|{}'.format(board['mid-L'], board['mid-M'], board['mid-R']))
    print('-+-+-')
    print('{}|{}|{}'.format(board['low-L'], board['low-M'], board['low-R']))

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for {}, move for wich space?'.format(turn))
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
        
printBoard(theBoard)
