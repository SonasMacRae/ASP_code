import random
import os
import math
import time
import snake as Snake


class Board:

    board = []
    pickup = (5,5)
    score = -1
    def __init__(self):
        self.CleanBoard()
        self.pickup = (5,5)

    def CleanBoard(self):
        self.board = []
        for x in range(10):
            self.board.append([])
            for y in range(10):
                self.board[x].append(str(y))

    def Render(self, snake, flag):
        self.CleanBoard()

        for x in snake.body:
            self.board[x[0]][x[1]] = "s"

        self.board[snake.head[0]][snake.head[1]] = "H"
        self.board[self.pickup[0]][self.pickup[1]] = "P"

        if flag == True:
            for x in range(10):
                for y in range(10):
                    if not self.board[x][y].isdigit():
                        print(" " + self.board[x][y] + " ", end = "")
                    else:
                        print(" _ ", end = "")
                print("")

    def SpawnPickup(self, snake):
        tiles = []
        self.score += 1
        for x in range(10):
            for y in range(10):
                if (x,y) not in snake:
                    temp = (x, y)
                    tiles.append(temp)
        temp = random.randint(0, len(tiles) - 1)
        self.pickup = tiles[temp]
