"""
    Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
    Программа должна вычислять сумму введенных элементов каждой строки
    и записывать ее в последнюю ячейку строки.
    В конце следует вывести полученную матрицу.
"""
import sys
from copy import copy

ROWS = 5
COLS = 4
SIZES = {}


def size(var):
    var_id = id(var)
    var_size = sys.getsizeof(var)
    if hasattr(var, '__iter__'):
        if hasattr(var, 'items'):
            for key, value in var:
                size(key)
                size(value)
        elif not isinstance(var, str):
            for item in var:
                size(item)
    SIZES.setdefault(var_id, [var_size, type(var), f'refcount={sys.getrefcount(var)}', f'{var=}'])
    if SIZES[var_id][0] != var_size:
        SIZES[var_id][0] = var_size


def sum_row(matrix):
    size(matrix)
    out = []
    for row_ in matrix:
        size(row_)
        r = copy(row_)
        sum_ = 0
        for n in r:
            sum_ += n
        else:
            size(n)
        sum_ = sum_
        size(sum_)
        r.append(sum_)
        size(r)
        out.append(r)
    size(out)
    return out


size(ROWS)
size(COLS)
data = []
for i in range(ROWS):
    row = []
    for x in input(f'Введите {COLS - 1} {"числа" if 2 <= (COLS - 1) <= 4 else "чисел"} через пробел: ').split():
        row.append(int(x))
    size(row)
    data.append(row)
else:
    size(x)
    size(i)

size(data)
sum_row(data)

# переменные для расчета не включаем, они не участвуют в основном коде программы
total = 0
for j, k in SIZES.items():
    total += k[0]
    # print(j, k)
print(f'{total=}')

# Введите 3 числа через пробел: 1 2 3
# Введите 3 числа через пробел: 4 5 6
# Введите 3 числа через пробел: 7 8 9
# Введите 3 числа через пробел: 10 11 12
# Введите 3 числа через пробел: 13 14 15
# Используем целые числа в матрице
# total=1835
