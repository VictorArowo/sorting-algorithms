def selection_sort(arr):
    for i in range(len(arr)):
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr
