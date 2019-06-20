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

def PathScores(board, snake, destination):
    tiles = []
    for x in range(10):
        tiles.append([])
        for y in range(10):
            tiles[x].append(Distance(destination,(x,y)))
            if(board[x][y] == "b"):
                tiles[x][y] = 999

    controls = ['w','s','a','d']
    scores = []

    head = snake[0]

    if len(snake) > 1:
        tiles[snake[1][0]][snake[1][1]] = 1100

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
    return controls[index]

def Bot(board, snake, simulationFlag):
    direction = "w"

    head = snake.head
    destination = (0,0)
    destination = board.pickup
    flag = True
    while flag:

        destination = board.pickup
        flag = snake.Move(PathScores(board.board, snake.body, destination), board)
        head = snake.head

        board.Render(snake, simulationFlag)

        if simulationFlag == True:
            time.sleep(0.05)
            os.system('cls||clear')




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
    print("Welcome to snake\n")
    print("1 Bot")
    print("2 You play")
    print("3 Bot simulation")

    temp = int(input())
    print(temp)

    if temp == 1:
        Bot(board, snake, True)
    if temp == 2:
        print("this is where we let the user play")
    if temp == 3:
        Simulation()

def Simulation():
    totalScore = 0
    iterations = 1000
    for x in range(iterations):
        if x % 50 == 0:
            print("%.0f%% complete" %((x/iterations)*100), end='\r')
        snake = s.Snake()
        board = b.Board()
        board.SpawnPickup(snake.body)
        Bot(board,snake, False)
        totalScore += board.score
    print("this is total score ", totalScore, "also average ", (totalScore/iterations))

Main()

# to do
# create a menu
# singleplayer, multiplayer, simulation
# need flags for when the simulation is run -> don't print the board
