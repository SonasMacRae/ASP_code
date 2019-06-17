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
