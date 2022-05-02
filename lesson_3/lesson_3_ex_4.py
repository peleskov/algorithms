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
for i, v in result.items():
    if v >= max_value:
        max_count = i
        max_value = v

print(f'Чаще всего ({max_count} {"раза" if 2 <= max_count <= 4 else "раз"}) в массиве встречается: {max_value}')
