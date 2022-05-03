"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random

RANGE_MIN = -10
RANGE_MAX = 10
RANGE_LEN = 10

range_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(0, RANGE_LEN)]
print(range_)


def min_():
    min_1 = None
    min_2 = None
    for i in range_:
        if min_1 is None:
            min_1 = i
        elif i < min_1:
            min_2, min_1 = min_1, i
        elif i > min_1:
            if min_2 is None:
                min_2 = i
            elif i < min_2:
                min_2 = i
    if min_2 is None:
        min_2 = min_1
    return min_1, min_2


print(f'Два наименьших элемента: {min_()}')

