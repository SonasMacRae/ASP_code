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
