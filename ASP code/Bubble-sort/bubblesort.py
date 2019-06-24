# Sorts an unsorted list using the bubble sort algorithm
def bubble(unsorted):
    # A flag that checks if the algorithm has swapped elements in this run
    swapped = True
    # If no swaps happen, the list is sorted, no need to loop
    while swapped:
        swapped = False
        # Loop through each element of the list (apart from the last)
        for i in range(0,len(unsorted)-1):
            # Another loop that checks the subset that follows
            # the current position
            for j in range(i+1, len(unsorted)):
                # If the one on the right is smaller than the one on the left
                # Swap them (list needs to be ascending)
                if unsorted[j] < unsorted[i]:
                    temp = unsorted[i]
                    unsorted[i] = unsorted[j]
                    unsorted[j] = temp
                    # A swap happened so list isn't sorted yet
                    swapped = True
    return unsorted



flag = True
list = []
# Reads input from command line
# In order to create a list to be swapped
while flag:
    i = int(input("enter number(-1 to stop): "))
    if i == -1:
        flag = False
    else:
        list.append(i)
print(list)
print(bubble(list))
