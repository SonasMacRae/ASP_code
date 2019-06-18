import random
import os
import math
import time
import board as b
import snake as s



snake = s.Snake()
board = b.Board()
board.SpawnPickup(snake.body)

def Distance(x, y):
    tempX = abs(x[0] - y[0])
    tempY = abs(x[1] - y[1])
    return (tempX + tempY)

def BodyPosition(snake, ele):
    for i in range(len(snake)):
        if snake[i] == ele:
            return len(snake) - i
    return 0
def PathScores(board, snake, destination):
    tiles = []
    for x in range(10):
        tiles.append([])
        for y in range(10):
            tiles[x].append(Distance(destination,(x,y)))
            if(board[x][y] == "■"):
                tiles[x][y] *= BodyPosition(snake,(x,y))
    controls = ['w','s','a','d']
    path = []
    head = snake[0]
    found = False
    if len(snake) > 1:
            tiles[snake[1][0]][snake[1][1]] = 1100
    while not found:
        scores = []
        # up
        upCoord = (head[0] -1, head[1])
        if upCoord[0] < 0:
            scores.append(1000)
        else:
            scores.append(tiles[upCoord[0]][upCoord[1]])

        # down
        downCoord = (head[0] + 1, head[1])
        if downCoord[0] > 9:
            scores.append(1000)
        else:
            scores.append(tiles[downCoord[0]][downCoord[1]])

        # left
        leftCoord = (head[0], head[1] - 1)
        if leftCoord[1] < 0:
            scores.append(1000)
        else:
            scores.append(tiles[leftCoord[0]][leftCoord[1]])

        # right
        rightCoord = (head[0], head[1] + 1)
        if rightCoord[1] > 9:
            scores.append(1000)
        else:
            scores.append(tiles[rightCoord[0]][rightCoord[1]])

        minScore = min(scores)
        index = scores.index(minScore)
        path.append(controls[index])
        if controls[index] == 'w':
            head = upCoord
        if controls[index] == 's':
            head = downCoord
        if controls[index] == 'a':
            head = leftCoord
        if controls[index] == 'd':
            head = rightCoord
        if head == destination:
            found = True
        else:
            print("more", end='')
    return path

def Bot(board, snake, simulationFlag):
    direction = "w"

    head = snake.head
    destination = (0,0)
    destination = board.pickup
    flag = True
    while flag:
        destination = board.pickup
        path = PathScores(board.board, snake.body, destination)
        print(path)
        for p in path:
            flag = snake.Move(p, board)
            head = snake.head
            board.Render(snake, simulationFlag)

            if simulationFlag == True:
                time.sleep(0.2)
                #print('\n' *5)
                #os.system('cls||clear')




def UserUpdate(board, snake):
    flag = True
    direction = "w"
    board.Render(snake, True)
    controls = ['w','a','s','d','q']
    while direction != "q" and flag:
        direction = input("move: ")
        if direction not in controls:
            continue
        flag = snake.Move(direction, board)

        os.system('cls||clear')
        board.Render(snake, True)

def Main():
    temp = 0
    while temp !=4:
        snake = s.Snake()
        board = b.Board()
        print("Welcome to snake\n")
        print("1 Bot")
        print("2 You play")
        print("3 Bot simulation")

        temp = int(input())

        if temp == 1:
            Bot(board, snake, True)
        if temp == 2:
            print("this is where we let the user play")
        if temp == 3:
            Simulation()
        if temp == 4:
            print("Bye!")

def Simulation():
    totalScore = 0
    highScore =0
    iterations = 20000
    for x in range(iterations):
        if x % 50 == 0:
            print("%.0f%% complete" %((x/iterations)*100), end='\r')
        snake = s.Snake()
        board = b.Board()
        board.SpawnPickup(snake.body)
        Bot(board,snake, False)
        if board.score > highScore:
            highScore = board.score
        totalScore += board.score
    print("this is total score ", totalScore, "also average ", (totalScore/iterations), " and the highest recorded run was: ", highScore)

Main()

# to do
# create a menu
# singleplayer, multiplayer, simulation
# need flags for when the simulation is run -> don't print the board
