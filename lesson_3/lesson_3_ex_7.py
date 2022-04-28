"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random
import time

RANGE_MIN = -10
RANGE_MAX = 10
RANGE_LEN = 10

range_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(0, RANGE_LEN)]
print(range_)


def quick_sort(array):
    if len(array) > 1:
        pivot = array.pop()
        left_lst, center_lst, right_lst = [], [pivot], []
        for i in array:
            if i == pivot:
                center_lst.append(i)
            elif i > pivot:
                right_lst.append(i)
            else:
                left_lst.append(i)
        return quick_sort(left_lst) + center_lst + quick_sort(right_lst)
    else:
        return array


range_sorted = quick_sort(range_)
print(f'Два наименьших элемента: {range_sorted[0:2]}')
