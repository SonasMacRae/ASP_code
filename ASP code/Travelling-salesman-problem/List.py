# This class holds the functions that interact with
# list of locations

import math
import random
import os

# Calculates Manhattan distance between two points
# a and b hold the x,y coordinates
def Distance(a, b):
    tempA = (a[0] - b[0]) ** 2
    tempB = (a[1] - b[1]) ** 2
    return math.sqrt(tempA + tempB)

# Calculates the distance of a path (list of points)
def TotalDistance(inputList):
    total = 0
    for x in range(len(inputList) - 1):
        total += Distance(inputList[x], inputList[x + 1])
    return total


def RandomCoordinates(length):
    tempList = []
    for x in range(length):
        temp = (random.randint(0, 100), random.randint(0, 100))
        while temp in tempList:
            temp = (random.randint(0, 100), random.randint(0, 100))
        tempList.append(temp)
    ViewList(tempList)
    return tempList

# Adds a new location to the list
def AddCity(locations):
    if len(locations) == 1000:
        print("You have hit the max size of the list\n")
        return locations
    temp = (random.randint(0, 100), random.randint(0, 100))
    if temp in locations:
        AddCity(locations)
    locations.append(temp)
    print("%s a city at coordinates " %RandomPhraseAdd(), temp)
    ViewList(locations)
    return locations


# Removes a new location to the list
def TakeAwayCity(locations):
    if len(locations) > 2:
        print("%s a city at coordinates " %RandomPhraseDestroy(), locations[-1])
        locations.pop()
    else:
        print("There has to be more than 1 location in the list")

    ViewList(locations)
    return locations


def AddButtLoads(locations):
    maxAdd = 1000 - len(locations)
    print("How many locations would you like to add?")
    print("(You can add up to ", maxAdd," locations)")
    temp = int(input())
    os.system('cls||clear')

    if temp > maxAdd:
        print("You tried to add too many locations\n")
        return locations

    for x in range(temp):
        locations = AddCity(locations)
    return locations



# Just for fun, everytime a location is removed, one of these
# words are used to describe how it got removed
def RandomPhraseDestroy():
    phrases = ["Destroyed","Demolished","Blew up","Nuked","Devastated","Kicked out","Abandoned"
    ,"Ravaged","Incinerated","Annihilated","Disintegrated","Wiped out","Ruined","Deserted","Eliminated",
    "Ended","Neglected","Discarded","Dumped"]
    return phrases[random.randint(0, len(phrases) - 1)]


# Just for fun, everytime a location is added, one of these
# words are used to describe how it got added
def RandomPhraseAdd():
    phrases = ["Built","Assembled","Completed","Manufactured","Produced","Put together","Created"
    ,"Constructed","Established","Produced","Whipped up","Threw together","Found","Created","Spawned",
    "Hatched","Fabricated","Made","Cooked up"]
    return phrases[random.randint(0, len(phrases) - 1)]


# UPDATE THIS
def ViewList(locations):
    print(locations)
    print("The number of locations in the list is: ",len(locations))
    print("\n")

def ResetList():
    originalList = [(1,6), (2,3), (3,7), (4,3), (6,2), (7,5), (9,8)]
    ViewList(originalList)
    return originalList
