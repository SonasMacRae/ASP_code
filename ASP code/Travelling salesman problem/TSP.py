# check the number of possible routes on google
# between n locations to be sure
# check if brute force goes back to the starting node



import math
import time
import random
import os
import copy
from itertools import permutations

locations = [(0,6), (1,3), (2,7), (3,3), (5,2), (6,5), (9,8)]

def Distance(x, y):
    tempX = (x[0] - y[0]) ** 2
    tempY = (x[1] - y[1]) ** 2
    return math.sqrt(tempX + tempY)


def TotalDistance(inputList):
    total = 0
    for x in range(len(inputList) - 1):
        total += Distance(inputList[x], inputList[x + 1])
    return total


def AddCity(locations):
    temp = (random.randint(0, 100), random.randint(0, 100))
    if temp in locations:
        AddCity(locations)
    locations.append(temp)
    print("%s a city at coordinates " %RandomPhraseAdd(), temp)
    ViewList(locations)
    return locations


def TakeAwayCity(locations):
    if len(locations) > 2:
        print("%s a city at coordinates " %RandomPhraseDestroy(), locations[-1])
        locations.pop()
    else:
        print("There has to be more than 1 location in the list")
    ViewList(locations)
    return locations


def RandomPhraseDestroy():
    phrases = ["Destroyed","Demolished","Blew up","Nuked","Devastated","Kicked out","Abandoned"
    ,"Ravaged","Incinerated","Annihilated","Disintegrated","Wiped out","Ruined","Deserted","Eliminated",
    "Ended","Neglected","Discarded","Dumped"]
    return phrases[random.randint(0, len(phrases) - 1)]


def RandomPhraseAdd():
    phrases = ["Built","Assembled","Completed","Manufactured","Produced","Put together","Created"
    ,"Constructed","Established","Produced","Whipped up","Threw together","Found","Created","Spawned",
    "Hatched","Fabricated","Made","Cooked up"]
    return phrases[random.randint(0, len(phrases) - 1)]


#make this look better
def ViewList(locations):
    print(locations)

def BruteForce(locations):
    start_time = time.time()
    p = permutations(locations)
    p = list(p)
    smallestIndex = 0
    smallestDistance = 999999

    counter = 0

    for x in p:
        if counter % 1000 == 0:
            print("%.2f%% complete" %(counter/len(p)*100),  end='\r')
        tempDistance = TotalDistance(x)
        if smallestDistance > tempDistance:
            smallestDistance = tempDistance
            smallestIndex = counter
        counter += 1

    print(p[smallestIndex], " is the path, the distance is %.2f" %smallestDistance)
    print("This process took %.4f seconds to complete" %int(time.time() - start_time))


def NearestNeighbour(locations):
    tempLocations = copy.deepcopy(locations)
    currentLocation = tempLocations[0]
    tempLocations.remove(currentLocation)
    totalDistance = 0
    while tempLocations:
        tempNearestNeighbour = currentLocation
        tempShortestDistance = 10000
        for x in tempLocations:
            if Distance(x, currentLocation) < tempShortestDistance:
                tempShortestDistance = Distance(x, currentLocation)
                tempNearestNeighbour = x
        currentLocation = tempNearestNeighbour
        tempLocations.remove(currentLocation)
        totalDistance += tempShortestDistance
    print("the total distance is ", totalDistance)
    print("number of locations in the list is ", len(locations))


def Run(locations):
    print("Select your method of calculating a path")
    print("1 - Brute force method")
    print("2 - Nearest neighbour")
    temp = input()

    if temp == "1":
        BruteForce(locations)
    if temp == "2":
        NearestNeighbour(locations)



def App(locations):
    print("\nWelcome to the TSP calculator\n")
    temp = ""
    while temp != "5":
        choice = False
        print("Input a number and press Enter to perform an action\n")
        print("1 - Calculate shortest path")
        print("2 - Add a city to the list")
        print("3 - Take away a city from the list")
        print("4 - View list")
        print("5 - Quit")
        temp = input()
        os.system('cls||clear')
        if temp == "1":
            Run(locations)
            choice = True

        if temp == "2":
            locations = AddCity(locations)
            choice = True

        if temp == "3":
            locations = TakeAwayCity(locations)
            choice = True

        if temp == "4":
            ViewList(locations)
            choice = True

        if temp == "5":
            print("Goodbye!")
            return

        if choice == False:
            print("Command not recognised, enter a number between 1 and 5")

App(locations)
