# Travelling salesman problem
The travelling salesman problem is a classic algorithmic problem in the field of computer science. The goal being to visit every location on a map and return to the starting location in the most efficient way. This may be defined by being the fastest, shortest or cheapest path, or a combination of all of these.

This problem is especially useful to demonstrate the power of planning solutions to problems, this activity shows how important it is to not always the best approach to dive head-first into a problem without giving it much thought.

The techniques used to demomnstrate this point are below:

## Environment
For this activity a 100x100 grid is used where locations are stored as (x,y) co-ordinates. Locations can be added or removed from the grid and at any point the co-ordinates of all of the locations can be viewed.

## Brute force method
This is one of the techniques used to find an optimal path between the locations. It works by calculating the length of all possible routes between the locations looking for the shortest route. 

TABLE
Pros -> Will always find the shortest route, Efficient if there are few locations to search

Cons -> Compile time gets exponentially longer the more locations are added, Can be memory intensive

The compile time of this brute force method on 5 locations is under 1 second, when the number of locations are around 20 or more, the compile time is years, at 100 locations the compile time is astronomical, by the time the script finishes compiling the Earth will be long gone...

