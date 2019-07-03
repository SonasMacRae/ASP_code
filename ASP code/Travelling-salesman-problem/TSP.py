import time
import os
import copy
import visual as V
import List as ListFunctions
from itertools import permutations


locations = [(1,6), (2,3), (3,7), (4,3), (6,2), (7,5), (9,8)]


def UpdateLocations(locations):
    temp = ""
    os.system('cls||clear')

    while temp != "Q" or temp != "q":
        choice = False

        print("How would you like to update the list\n")
        print("1 - Add 1 new location")
        print("2 - Take away 1 location")
        print("3 - I want to add a butt load of locations")
        print("4 - Change the co-ordinates of all the locations randomly")
        print("5 - Reset list")
        print("Q - Go back")

        temp = input()
        os.system('cls||clear')

        if temp == "1":
            locations = ListFunctions.AddCity(locations)
            choice = True

        if temp == "2":
            locations = ListFunctions.TakeAwayCity(locations)
            choice = True

        if temp == "3":
            locations = ListFunctions.AddButtLoads(locations)
            choice = True

        if temp == "4":
            locations = ListFunctions.RandomCoordinates(len(locations))
            choice = True

        if temp == "5":
            locations = ListFunctions.ResetList()
            choice = True

        if temp == "Q" or temp == "q":
            return locations

        if choice == False:
            print("Command not recognised, enter a number between 1 and 4\n")


# Brute force way of getting best path
def BruteForce(locations):
    start_time = time.time()
    # Gets all the path combinations
    p = permutations(locations)
    p = list(p)
    smallestIndex = 0
    smallestDistance = 999999

    counter = 0
    # Go through all the paths
    for x in p:
        x = list(x)
        x.append(x[0])
        if counter % 1000 == 0:
            print("%.2f%% complete" %(counter/len(p)*100),  end='\r')
        # gets the path distance
        tempDistance = ListFunctions.TotalDistance(x)
        # if this path is shorter than previous best, remember this
        if smallestDistance > tempDistance:
            smallestDistance = tempDistance
            smallestIndex = counter
        counter += 1

    path = []
    for x in p[smallestIndex]:
        path.append(x)
    path.append(p[smallestIndex][0])

    # prints smallest distance found
    print(path, " is the path, the distance is ", smallestDistance)
    print("This process took %.4f seconds to complete" %int(time.time() - start_time))

    V.DisplayRoute(path)


# NN algorithm for finding a path
def NearestNeighbour(locations):
    start_time = time.time()
    shortDistance = 100000
    path = []
    counter = 0
    for x in locations:
        counter += 1
        if counter % 10 == 0:
            print("%.2f%% complete" %(counter/len(locations)*100), end='\r')
        tempPath = []
        tempLocations = copy.deepcopy(locations)
        currentLocation = x
        tempLocations.remove(currentLocation)
        tempPath.append(x)
        totalDistance = 0

        while tempLocations:
            tempNearestNeighbour = currentLocation
            tempShortestDistance = 10000

            for x in tempLocations:
                if ListFunctions.Distance(x, currentLocation) < tempShortestDistance and ListFunctions.Distance(x, currentLocation) != 0:
                    tempShortestDistance = ListFunctions.Distance(x, currentLocation)
                    tempNearestNeighbour = x
            currentLocation = tempNearestNeighbour
            tempLocations.remove(currentLocation)
            tempPath.append(currentLocation)
            totalDistance += tempShortestDistance

            if len(tempLocations) == 0:
                tempPath.append(tempPath[0])
                totalDistance += ListFunctions.Distance(tempPath[len(tempPath) - 1], tempPath[len(tempPath) - 2])

        if totalDistance < shortDistance:
            shortDistance = totalDistance
            path = tempPath

    print("the total distance is ", shortDistance, " path is ",path)
    print("This process took %.4f seconds to complete" %int(time.time() - start_time))

    V.DisplayRoute(path)


def Run(locations):
    temp = ""
    while temp != "Q":
        os.system('cls||clear')
        choice = False

        print("Select your method of calculating a path\n")
        print("1 - Brute force method")
        print("2 - Nearest neighbour")
        print("Q - Go back")

        temp = input()
        os.system('cls||clear')

        if temp == "1":
            BruteForce(locations)
            choice = True

        if temp == "2":
            NearestNeighbour(locations)
            choice = True

        if temp == "Q" or temp == "q":
            return

        if choice == False:
            print("Command not recognised, enter a number between 1 and 2\n")


def App(locations):
    os.system('cls||clear')
    print("Welcome to the TSP calculator\n")
    temp = ""
    while temp != "Q":
        os.system('cls||clear')
        choice = False
        print("Input a number and press Enter to perform an action\n")
        print("1 - Calculate shortest path")
        print("2 - Update locations list")
        print("3 - View locations list")
        print("Q - Quit")

        temp = input()
        os.system('cls||clear')
        if temp == "1":
            Run(locations)
            choice = True

        if temp == "2":
            locations = UpdateLocations(locations)
            choice = True

        if temp == "3":
            ListFunctions.ViewList(locations)
            V.ShowPositions(locations)
            choice = True

        if temp == "Q" or temp == "q":
            print("Goodbye!")
            return

        if choice == False:
            print("Command not recognised, enter a number between 1 and 3\n")

App(locations)
