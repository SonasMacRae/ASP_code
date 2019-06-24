# Prompt user for int input
size = int(input("Enter the size of the tree: "))

print("")
print("")

# Initialise the number of blanks and stars
stars = 1
blank = size - 1

# This is the height of the tree
for x in range(size):
    # String to be built for the current line, will contain the 
    # blanks and the stars
    row = ""

    # The number of blanks to be printed for the current line
    for y in range(blank):
        row += " "

    # The number of stars to be printed on the current line
    for y in range(stars):
        row += "*"

    # Prints the string representing the current row
    print(row)

    # For each new line the number of blanks decreases by 1 and the
    # number of stars increases by 2
    blank -= 1
    stars += 2

# This prints the base of the tree
for x in range(size - 1):
    # end="" stops a newline from being printed from the print statement
    print(" ", end = "")
print("*")

print("")
print("")
