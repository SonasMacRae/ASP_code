# Python cheat sheet
# (This is a comment)

# Define variables (in Python you don't have to
# specify the type of variable, but you can cast between types)
variable = 5
variable2 = 3.5
variable3 = "this is a string"
variable4 = ["this", "is", "a", "list"]
variable5 = int("123")

# Print statements
print("This is a print statement")
print(variable3)
print(variable4[0])
print(variable + variable2)

# User input (from the console)
userInput = input("Enter an input")
# You can then print the user input
print(userInput)

# Math stuff
newNumber = 5 + 5
newNumber = 5 - 5
newNumber = 5 / 5
newNumber = 5 * 5
newNumber = 10 % 4  # (This is remainder)

# If statements
if 2 < 5:
    print("2 is less than 5")
else:
    print("2 is not less than 5")

if 1 == 1 and 2 < 5:
    print("True")

if 1 == 2 or 1 == 1:
    print("True")

# Loops
for x in range(10):
    print(x)
for x in range(5, 10):
    print(x)
for x in variable4:
    print(x)

# Functions
def PrintInput(example):
    print(example)

def Math(x,y):
    if not str(x).isdigit() or not str(y).isdigit():
        print("The inputs must be integers")
        return
    return x + y

# Recursion is a type of function that calls itself
# it can be very useful when used correctly
def Recursion(x):
    if not str(x).isdigit():
        print("The input must be an positive integer")
        return x

    if x == 100:
        return x

    if x > 100 or x < 0:
        return Recursion(0)

    x += 1

    return Recursion(x)

# Calling functions
PrintInput("Hello world!")
print(Math(5,10))
print(Recursion(10))
