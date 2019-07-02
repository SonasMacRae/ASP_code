# How to use the application

**To use this application you need to install Matplotlib**
<a href="https://matplotlib.org/#" target="_blank">Matplotlib website</a>


This application runs on the **terminal/command line**, open up your **terminal/command line** and navigate to the folder which holds this application and enter **python TSP.py** 

navigate the menu's by entering the corresponding number into the terminal and press enter.
This application is used to demonstrate the processing speed between two different methods when calculating an optimal path between a set of nodes on a grid.

# Travelling salesman problem
The travelling salesman problem is a classic algorithmic problem in the field of computer science. The goal being to visit every location on a map and return to the starting location in the most efficient way. This may be defined by being the fastest, shortest or cheapest path, or a combination of all of these.

This problem is especially useful to demonstrate the power of planning solutions to problems, this activity shows how important it is to not always the best approach to dive head-first into a problem without giving it much thought.

The techniques used to demomnstrate this point are below:

## Environment
For this activity a 100x100 grid is used where locations are stored as (x,y) co-ordinates. Locations can be added or removed from the grid and at any point, the co-ordinates of all of the locations can be viewed.

## Brute force method
This is one of the techniques used to find an optimal path between the locations. It works by calculating the length of all possible routes between the locations looking for the shortest route. 

<img width="689" alt="Screenshot 2019-06-13 at 13 34 41" src="https://user-images.githubusercontent.com/36636474/59432805-166ddc00-8de0-11e9-8851-10b82b8d3fdb.png">

The compile time of this brute force method on 5 locations is under 1 second, when the number of locations are around 20 or more, the compile time is years, at 100 locations the compile time is astronomical, by the time the script finishes compiling the Earth will be long gone...

Note: The algorithm written to demonstrate this has to add every possible path to a list before it can start calculating the shortest route, nothing is displayed whilst this happens, the more permuatations there are to calculate the longer the wait is.

## Nearest neighbour method
Because the last method is incredibly unefficient for calculating a route for a large number of locations, the nearest neighbour technique is one that is much more appropriate for these types of problems.

This works by travelling to the nearest neighbour until there are no more locations to travel to.
The nearest neighbour technique won't always find the most efficient path, but it will find a soluition in an appropriate amount of time when working with a large number of locations. 

<img width="524" alt="Screenshot 2019-06-13 at 14 17 36" src="https://user-images.githubusercontent.com/36636474/59435697-0f49cc80-8de6-11e9-8772-2aecc0c386f5.png">


