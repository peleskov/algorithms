from random import randint

RANGE = [0, 100]
LEN = 4


def get_median(arr):
    # gnome sort
    i = 1
    j = 2
    while i < len(arr):
        if arr[i - 1] < arr[i]:
            i = j
            j = j + 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i = i - 1
            if i == 0:
                i = j
                j = j + 1
    return arr[len(arr) // 2]


numbers = [randint(RANGE[0], RANGE[1]) for _ in range(LEN*2 + 1)]
print(numbers)
median = get_median(numbers)
print(median)

