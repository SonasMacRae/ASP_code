# Bubble Sort

For this challenge, the goal is to write the simple sort algorithm: bubble sort. For those unfamiliar, bubble sort works by repeatedly stepping through the list, compares adjacent pairs and swaps them if they are in the wrong order.
### Example:
![bubblesort](http://miftyisbored.com/wp-content/uploads/2015/01/bubble-sort-demo.jpg)

# Name surrounded by stars challenge

In this challenge, the goal is to write an application that prompt the user for an input, before outputting the input surrounded by stars, an example output is:

<img width="291" alt="Screenshot 2019-06-06 at 11 50 36" src="https://user-images.githubusercontent.com/36636474/59027759-caf08680-8851-11e9-8764-106fadc04c2e.png">

You may write this in any langauge, although the solution is written in Python.


## Pseudocode

temp = <b>PROMPT</b> user for input<br/>
output = ""<br/>
<b>LOOP</b> (length(temp)+4):<br/>
&nbsp;&nbsp;&nbsp;output = output + "*"<br/>
<b>END LOOP</b><br/>
<b>PRINT</b>(output)<br/>
<b>PRINT</b>("\* temp *")<br/>
<b>PRINT</b>(output)<br/>


# Prime numbers challenge (slightly more difficult than the last challenge)

What is the sum of all of the prime numbers below 10,000 whose digits are all prime numbers themselves. 
An example would be '3257' since it is a prime number and all of its digits '3','2','5' and '7' are all prime numbers.

For those of you who have been through and completed some of the examples from https://projecteuler.net this may be trivial. 

## Cheats

Because you may not have enough time to complete this challenge without any help along with the other challenges and activities, code to detect prime numbers in Python is available below.

<img width="528" alt="Screenshot 2019-06-11 at 20 45 33" src="https://user-images.githubusercontent.com/36636474/59301770-4d31de00-8c8a-11e9-801d-428bf6bbd6f0.png">


# Snake
This is a project that was developed by two third year Computing Science students who had too much spare time.

## What actually is it?
It's a bot that plays a traditional snake game, this application has 2 modes:
- Bot (where you can watch the bot play the game)
- Simulation (where the bot plays the game over and over again at a very high speed, the average and high score is recorded)

## What is the point of this?
I'm glad you asked, the purpose of this is to demonstrate what can be achieved from the knowledge gained at University. This project also shows that you can have fun, it is possible to create projects of your interest and that there is nothing stopping you. 

We have made the code from this project accessible for anyone to look at and play around with.

## How does it work?
Well, the goal for the snake is to eat fruit and avoid death

![Snake](https://i.imgur.com/RSj70JC.gif)

The board is a 10x10 grid, initially each square is assigned a value equal to its manhattan distance from the fruit. Squares which the snake is occupying have a score higher than any other square. The bot moves the head of the snake to the lowest scoring neighbour, this will naturally gravitate the snake towards the fruit and stop it from trying to eat itself and die (most of the time)


# How to use the application
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


# Tree printing challenge

Using the terminal/command line of your computer, prompt the user for an input before printing the input surrounded by stars.

A solution to this problem was written in python and is available to look at, although it is advised that you try this for yourself before looking at the solution.

The image below demonstrates what it should look like:

<img width="450" alt="Screenshot 2019-06-16 at 13 36 57" src="https://user-images.githubusercontent.com/36636474/59564229-0baf8300-903c-11e9-849b-f0753f5d34bc.png">
