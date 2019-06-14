def bubble(unsorted):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0,len(unsorted)-1):
            for j in range(i+1, len(unsorted)):
                if unsorted[j] < unsorted[i]:
                    temp = unsorted[i]
                    unsorted[i] = unsorted[j]
                    unsorted[j] = temp
                    swapped = True
    return unsorted



flag = True
list = []
while flag:
    i = int(input("enter number(-1 to stop): "))
    if i == -1:
        flag = False
    else:
        list.append(i)
print(list)
print(bubble(list))
