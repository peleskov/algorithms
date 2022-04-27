"""
    В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

RANGE_MIN = -100
RANGE_MAX = 100
RANGE_LEN = 10

range_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(0, RANGE_LEN)]
print(range_)

max_ = [0, range_[0]]  # index, value
min_ = [0, range_[0]]
for n, i in enumerate(range_):
    if i < min_[1]:
        min_ = [n, i]
    elif i > max_[1]:
        max_ = [n, i]

range_[min_[0]],  range_[max_[0]] = range_[max_[0]], range_[min_[0]]
print(range_)
print(min_, max_)
