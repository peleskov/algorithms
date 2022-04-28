"""
    Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random

ROWS = 3
COLS = 4
MIN = -100
MAX = 100
matrix = [[random.randint(MIN, MAX) for _ in range(0, COLS)] for _ in range(0, ROWS)]
for row in matrix:
    for i in row:
        print(f'{i:>5}', end='')
    print('')

min_list = [None] * len(matrix[0])
for row in matrix:
    for i, v in enumerate(row):
        if min_list[i] is None or v < min_list[i]:
            min_list[i] = v

print(min_list)
max_min = min_list[0]
for i in min_list:
    if i > max_min:
        max_min = i

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_min}')