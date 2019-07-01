# Author: Sonas MacRae
# Last modified: 29/05/2019

# Step 1 - Prompt the user for an input, save this input
# into the variable userInput
userInput = input("Enter an input: ")

# Step 2 - Create a string which will be concatenated to.
outputString = ""

# The output string will be the lines above and below the
# input string, which is 4 characters longer than the userInput.
# Create a loop 4 iterations longer than the length of the input
# concatenating a star to the outputString with each iteration.
for x in range(len(userInput) + 4):
    outputString += "*"

# Step 3 - Print
print(outputString)

print("* ", userInput, " *")

print(outputString)
