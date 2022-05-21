from random import randint

RANGE = [-100, 100]
LEN = 10


def bubble_sort(arr):
    for n in range(LEN):
        stop = True
        for i in range(LEN-1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                stop = False
        if stop:
            break
    return


numbers = [randint(RANGE[0], RANGE[1] - 1) for _ in range(LEN)]
print(numbers)
print('*' * 50)
bubble_sort(numbers)
print(numbers)
