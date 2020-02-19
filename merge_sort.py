def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    if len(arrA) == 0:
        return arrB
    if len(arrB) == 0:
        return arrA

    a_index = 0
    b_index = 0

    while len(merged_arr) < elements:
        if arrA[a_index] <= arrB[b_index]:
            merged_arr.append(arrA[a_index])
            a_index += 1
        else:
            merged_arr.append(arrB[b_index])
            b_index += 1

        if a_index == len(arrA):
            merged_arr += arrB[b_index:]
            break
        elif b_index == len(arrB):
            merged_arr += arrA[a_index:]
            break

    return merged_arr


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left, right = arr[:middle], arr[middle:]
        return merge(merge_sort(left), merge_sort(right))
