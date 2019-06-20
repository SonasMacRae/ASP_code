size = int(input("Enter the size of the tree: "))
print("")
print("")

stars = 1
blank = size - 1

for x in range(size):
    row = ""

    for y in range(blank):
        row += " "

    for y in range(stars):
        row += "*"

    print(row)

    blank -= 1
    stars += 2

for x in range(size - 1):
    print(" ", end = "")
print("*")
print("")
print("")
