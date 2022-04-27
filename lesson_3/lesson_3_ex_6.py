"""
    В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
    Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

RANGE_MIN = -10
RANGE_MAX = 10
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

sum_ = 0
if abs(max_[0] - min_[0]) > 1:
    pos = (max_[0], min_[0]) if min_[0] > max_[0] else (min_[0], max_[0])
    for i in range(pos[0] + 1, pos[1]):
        sum_ += range_[i]
    print(pos)

print(sum_)