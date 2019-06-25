import copy

# calculates unavailable squares
def blockedSquares(board):
    count = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] != 0:
                count += 1
    return count

# calculates potential unavailable squares for a new move
def squareScore(board, queen):
    tempBoard = copy.deepcopy(board)
    for i in range(8):
        # positions a queen can go to (fw, bw, sideways, diagonal)
        positions = [(0, -i), (0, i), (-i, 0), (i, 0), (i, i), (-i,-i), (i,-i), (-i, i)]
        for p in positions:
            newPosition = (queen[0] + p[0], queen[1] + p[1])
            if((newPosition[0] < 8 and newPosition[0] >= 0) and (newPosition[1] < 8 and newPosition[1] >= 0)):
                tempBoard[newPosition[0]][newPosition[1]] = 1
    return blockedSquares(tempBoard)

# adds a new queen to the board
# qList is the list of the queens currently placed
# blackList stores postions that won't produce a final result (even though they have a low score)
def addQueen(board, qList, blackList):
    # keeps track of best queen position
    best = 65
    bestCoord = (9,9)
    # gets the current ammount of blocked squares
    squares = blockedSquares(board)
    for x in range(8):
        for y in range(8):
            if board[x][y] == 0:
                # calculates the score of the empty position
                score = squareScore(board, (x,y))
                # if it's smaller than current best score (and not blacklisted), keep track of this new coordinate
                if (score - squares < best) and ((x,y) not in blackList):
                    best = score - squares
                    bestCoord = (x,y)
    # add the new queen to the list
    qList.append(bestCoord)
    return qList

# updates the board with a new queen
# and notes the squares it can go to
def updateBoard(board, queen):
    for i in range(8):
        positions = [(0, -i), (0, i), (-i, 0), (i, 0), (i, i), (-i,-i), (i,-i), (-i, i)]
        for p in positions:
            newPosition = (queen[0] + p[0], queen[1] + p[1])
            if((newPosition[0] < 8 and newPosition[0] >= 0) and (newPosition[1] < 8 and newPosition[1] >= 0)):
                board[newPosition[0]][newPosition[1]] = 1
    board[queen[0]][queen[1]] = 3
    return board
# prints chess board on screen
def printBoard(board):
    for x in range(8):
        print("")
        for y in range(8):
            if board[x][y] == 1 or board[x][y] == 0:
                print(" _ ", end="")
            else:
                print(" Q ", end="")
# resets board
def cleanBoard(board):
    for x in range(8):
        board.append([])
        for y in range(8):
            board[x].append(0)
    return board


def Main():
    board = cleanBoard([])
    blackListed = []
    flag = True
    while flag:
        board = cleanBoard([])
        queenList = []
        flag = False
        for i in range(8):
            queenList = addQueen(board, queenList, blackListed)
            # if last element is 9,9 then a solution couldn't be found
            if queenList[i] == (9,9):
                #blacklist first queen coordinate
                blackListed.append(queenList[0])
                flag = True
                break
            board = updateBoard(board, queenList[i])
    printBoard(board)

Main()