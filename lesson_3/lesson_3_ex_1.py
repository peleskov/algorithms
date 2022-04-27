"""
    В диапазоне натуральных чисел от 2 до 99 определить,
    сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

RANGE1_START = 2
RANGE1_END = 99
RANGE2_START = 2
RANGE2_END = 9

range1 = [_ for _ in range(RANGE1_START, RANGE1_END + 1)]
range2 = [_ for _ in range(RANGE2_START, RANGE2_END + 1)]

multiples = []
for i in range2:
    k = 0
    for j in range1:
        if j % i == 0:
            k += 1
    multiples.append((i, k))

for i, k in multiples:
    print(f'числу {i} кратно {k} {"число" if k == 1 else "числа" if 2<= k <= 4 else "чисел"}')
