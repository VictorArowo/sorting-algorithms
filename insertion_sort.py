def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


def recursive_insertion_sort(arr, n):
    if n <= 1:
        return

    recursive_insertion_sort(arr, n-1)
    final = arr[n-1]
    j = n-2

    while (j >= 0 and arr[j] > final):
        arr[j+1] = arr[j]
        j = j-1

    arr[j+1] = final
