def bubble_iterative(arr):
    length = len(arr)

    for i in range(length):
        swapped = False

        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True

        if(swapped == False):
            break

    return arr


print(bubble_iterative([4, 100, 90, 53, 22, 3, 6, 2, 1, 10, 9, 3]))


def bubble_recursive(arr, length=None):
    if length == None:
        length = len(arr) - 1
    if length <= 1:
        return arr

    for i in range(length):
        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]

    return bubble_recursive(arr, length-1)


print(bubble_recursive([4, 100, 90, 53, 22, 3, 6, 2, 1, 10, 9, 3]))
