from random import uniform

RANGE = [0, 50]
LEN = 10


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = len(arr) // 2
    arr_1 = merge_sort(arr[:pivot])
    arr_2 = merge_sort(arr[pivot:])
    return merge(arr_1, arr_2)


def merge(arr_1, arr_2):
    result = []
    while arr_1 and arr_2:
        if arr_1[0] <= arr_2[0]:
            result.append(arr_1[0])
            arr_1 = arr_1[1:]
        else:
            result.append(arr_2[0])
            arr_2 = arr_2[1:]
    if arr_1:
        result += arr_1
    if arr_2:
        result += arr_2
    return result


numbers = [round(uniform(RANGE[0], RANGE[1] - 1), 2) for _ in range(LEN)]
print(numbers)
numbers_sorted = merge_sort(numbers)
print(numbers_sorted)
