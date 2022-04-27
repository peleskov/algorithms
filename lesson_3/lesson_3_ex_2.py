"""
    Во втором массиве сохранить индексы четных элементов первого массива.
    Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
    второй массив надо заполнить значениями 0, 3, 4, 5,
    (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""
import random

RANGE_MIN = 0
RANGE_MAX = 100
RANGE_LEN = 20

range_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(0, RANGE_LEN + 1)]
print(range_)

result = []
for n, val in enumerate(range_):
    if val % 2 == 0:
        result.append(n)

print(result)
