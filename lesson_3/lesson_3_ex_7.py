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

res = [None, None]
for i in range_:
    if res[0] is None or i < res[0]:
        res[1], res[0] = res[0], i
    elif res[1] is None or i == res[0] or i < res[1]:
        res[1] = i

print(f'Два наименьших элемента: {res}')

