# This class creates and displays graphs to illustrate solutions

import matplotlib.pyplot as plt

# Used to show the positions of the locations on the grid
def ShowPositions(locations):
    locationsx = []
    locationsy = []

    for x in range(len(locations)):
        locationsx.append(locations[x][0])
        locationsy.append(locations[x][1])

    plt.scatter(locationsx,locationsy)
    plt.title('Travelling salesman problem')

    print("\nYou must close the graph before carrying on\n")
    
    plt.show()


# Shows the route taken between all of the points on the grid
def DisplayRoute(locations):
    locationsx = []
    locationsy = []

    for x in range(len(locations)):
        locationsx.append(locations[x][0])
        locationsy.append(locations[x][1])

    plt.title('Travelling salesman problem')

    plt.scatter(locationsx,locationsy)
    plt.plot(locationsx,locationsy)

    print("\nYou must close the graph before carrying on\n")

    plt.show()
