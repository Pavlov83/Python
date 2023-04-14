


def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while (first <= last):

        middle = (first + last) // 2
        if (list[middle] == target):
            return middle
        elif (list[middle] < target):
            first = middle + 1
        else:
            last = middle - 1

    return None


def verify(item):
    if (item != None):
        print("The item is on index", item)
    else:
        print("The item is not in the list")


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

result = binary_search(myList, 6)

verify(result)