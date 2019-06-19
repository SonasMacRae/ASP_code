import random
import os
import math
import time
import board as b
import snake as s
import node as n


snake = s.Snake()
board = b.Board()
board.SpawnPickup(snake.body)

def BodyPosition(snake, ele):
    for i in range(len(snake)):
        if snake[i] == ele:
            return len(snake)
    return 0

def PathScores(board,snake, destination):
    start = snake[0]
    maze = []
    for x in range(10):
        maze.append([])
        for y in range(10):
            if board[x][y].isdigit():
                maze[x].append(0)
            else:
                maze[x].append(BodyPosition(snake,(x,y)))
    moves = n.astar(maze,start,destination)
    controls = ['a','d','s','w']
    positions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    path = []
    current = moves[0]
    for i in range(1,len(moves)):
        m = moves[i]
        for j in range(len(positions)):
            if (m[0] + positions[j][0]) == current[0] and (m[1]+ positions[j][1] == current[1]):
                current = moves[i]
                path.append(controls[j])
                break

    return path


def Bot(board, snake, simulationFlag):
    direction = "w"
    head = snake.head
    flag = True
    while flag:
        destination = board.pickup
        path = PathScores(board.board, snake.body, destination)
        for p in path:
            time.sleep(0.2)
            os.system('cls||clear')
            flag = snake.Move(p, board)
            head = snake.head
            board.Render(snake, simulationFlag)

        #if not simulationFlag == True:
            #time.sleep(0.2)
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
