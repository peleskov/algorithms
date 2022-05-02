"""
    Определить, какое число в массиве встречается чаще всего.
"""
import random
import timeit
import cProfile

RANGE_MIN = -10
RANGE_MAX = 10
RANGE_LEN = 10

range_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(0, RANGE_LEN)]
print(range_)

result = {}

for i in range_:
    result.setdefault(i, 0)
    result[i] += 1

max_count = 0
max_value = 0
for v, i in result.items():
    if i >= max_count:
        max_count = i
        max_value = v

if max_count == 1:
    print('Все числа встречаются 1 раз')
else:
    print(f'Чаще всего ({max_count} {"раза" if 2 <= max_count <= 4 else "раз"}) в массиве встречается: {max_value}')
