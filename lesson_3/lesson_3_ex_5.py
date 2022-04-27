"""
    В массиве найти максимальный отрицательный элемент.
    Вывести на экран его значение и позицию в массиве.
    Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
    Это два абсолютно разных значения.
"""
import random

RANGE_MIN = -10
RANGE_MAX = 10
RANGE_LEN = 10

range_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(0, RANGE_LEN + 1)]
print(range_)

max_negative = None
for n, i in enumerate(range_):
    if max_negative is None and i < 0:
        max_negative = [n, i]
    if max_negative and 0 > i > max_negative[1]:
        max_negative = [n, i]

print(f'Максимальное отрицательное число {max_negative[1]} на позиции {max_negative[0]}' if max_negative
      else 'Нет отрицательных чисел')
