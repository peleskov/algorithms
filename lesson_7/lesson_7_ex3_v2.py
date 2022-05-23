from random import randint, choice

RANGE = [0, 100]
LEN = 4


def get_median(arr, index=None):
    if index is None:
        index = len(arr) // 2

    pivot = choice(arr)
    arr_1 = [i for i in arr if i < pivot]
    arr_2 = [i for i in arr if i > pivot]
    arr_3 = [i for i in arr if i == pivot]

    if index < len(arr_1):
        return get_median(arr_1, index)
    elif index < len(arr_1) + len(arr_3):
        return pivot
    else:
        return get_median(arr_2, index - len(arr_1) - len(arr_3))


numbers = [randint(RANGE[0], RANGE[1]) for _ in range(LEN * 2 + 1)]
print(numbers)
median = get_median(numbers)
print(median)
