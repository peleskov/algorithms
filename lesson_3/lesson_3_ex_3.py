"""
    В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

RANGE_MIN = -100
RANGE_MAX = 100
RANGE_LEN = 10

range_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(0, RANGE_LEN)]
print(range_)

max_index, max_val = 0, range_[0]
min_index, min_val = 0, range_[0]
for n, i in enumerate(range_):
    if i < min_val:
        min_index, min_val = n, i
    elif i > max_val:
        max_index, max_val = n, i

range_[min_index],  range_[max_index] = range_[max_index], range_[min_index]
print(range_)
print(f'{min_index=}', f'{min_val=}')
print(f'{max_index=}', f'{max_val=}')
