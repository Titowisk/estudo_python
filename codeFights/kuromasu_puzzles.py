#

board = [['*', '.', '#', '.', '.', '*', '.', '.', '#', '.', '.'],
         ['.', '*', '.', '.', '*', '.', '*', '.', '#', '.', '.'],
         ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#'],
         ['#', '.', '.', '.', '.', '.', '.', '*', '.', '*', '.'],
         ['*', '#', '.', '.', '*', '.', '.', '.', '*', '.', '.'],
         ['.', '.', '#', '.', '#', '.', '#', '*', '#', '.', '.'],
         ['.', '.', '*', '.', '.', '.', '.', '.', '*', '#', '*'],
         ['.', '.', '.', '.', '*', '.', '*', '.', '.', '*', '#'],
         ['#', '.', '*', '.', '.', '*', '#', '.', '*', '.', '.'],
         ['.', '.', '#', '.', '.', '.', '*', '.', '.', '.', '.'],
         ['.', '*', '#', '*', '.', '*', '.', '.', '#', '.', '*']]

line = len(board)
columns = len(board[0])
new_board = []
for i in range(line):
    new_board.append([])
    for j in range(columns):
        new_board[i].append(0)
        if board[i][j] == "#":
            c = 0
            # lef
            x = j-1
            while x >= 0:  # (0, 3)
                if board[i][x] == '.' or board[i][x] == '#':
                    c += 1
                if board[i][x] == '*':
                    break
                x -= 1
            # right
            y = j+1
            while y <= line-1:  # (0, 3)
                if board[i][y] == '.' or board[i][y] == '#':
                    c += 1
                if board[i][y] == '*':
                    break
                y += 1
            # down
            for d in range(i+1, line):
                if board[d][j] == '.' or board[d][j] == '#':
                    c += 1
                if board[d][j] == '*':
                    break
            # up
            for u in range(i-1, -1, -1):
                if board[u][j] == '.' or board[u][j] == '#':
                    c += 1
                if board[u][j] == '*':
                    break
            # valor da '#'
            new_board[i][j] = c + 1
        if board[i][j] != "#":
            new_board[i][j] = -1


for l in new_board:
    print(l)

print('-----------------------------------------------------')

for l in board:
    print(l)