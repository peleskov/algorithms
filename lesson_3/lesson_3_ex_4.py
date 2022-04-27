"""
    Определить, какое число в массиве встречается чаще всего.
"""
import random

RANGE_MIN = -10
RANGE_MAX = 10
RANGE_LEN = 10

range_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(0, RANGE_LEN)]
print(range_)

result = {}

for i in range_:
    result.setdefault(i, 0)
    result[i] += 1

max_ = 0
for m in result.values():
    if m >= max_:
        max_ = m

print(f'Чаще всего ({max_} {"раза" if 2 <= max_ <= 4 else "раз"}) в массиве встречается: ')
for k, v in result.items():
    if v == max_:
        print(k)
