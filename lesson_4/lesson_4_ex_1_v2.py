"""
    Урок 3 задача 7
    В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random
import timeit
import cProfile
import matplotlib.pyplot as plt


def min_(r_min, r_max, r_len):
    range_ = [random.randint(r_min, r_max) for _ in range(r_len)]
    range_sorted = quick_sort(range_)
    return range_sorted[:2]


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


num_tests = 10  # количество тестов
result = []
for var in [i * 1000 for i in range(1, num_tests + 1)]:  # изменяем диапазон чисел и длину массива
    test = timeit.timeit(f"min_({var * (-1)}, {var}, {var})", number=1000, globals=globals())
    result.append(test)
    print(f'min_({var * (-1)}, {var}, {var}) - {test}')

plt.plot(result)
plt.savefig('./lesson_4_ex_1_v2_chart.jpg')

print("cProfile.run(f'min_(-1_000_000, 1_000_000, 1_000_000)')")
cProfile.run(f'min_(-1_000_000, 1_000_000, 1_000_000)')

#
# min_(-1000, 1000, 1000)   -  1.3685262999497354
# min_(-2000, 2000, 2000)   -  2.8285630000173114
# min_(-3000, 3000, 3000)   -  4.481590499985032
# min_(-4000, 4000, 4000)   -  6.153779899992514
# min_(-5000, 5000, 5000)   -  7.980420400039293
# min_(-6000, 6000, 6000)   -  9.701360999955796
# min_(-7000, 7000, 7000)   - 11.391012200037949
# min_(-8000, 8000, 8000)   - 13.079735599982087
# min_(-9000, 9000, 9000)   - 14.926024800050072
# min_(-10000, 10000, 10000)- 16.647122299997136


# cProfile.run(f'min_(-1_000_000, 1_000_000, 1_000_000)')
#          34985407 function calls (33867869 primitive calls) in 7.615 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.029    0.029    7.615    7.615 <string>:1(<module>)
#         1    0.006    0.006    7.585    7.585 lesson_4_ex_1_v2.py:12(min_)
#         1    0.200    0.200    1.783    1.783 lesson_4_ex_1_v2.py:13(<listcomp>)
# 1117539/1    4.355    0.000    5.796    5.796 lesson_4_ex_1_v2.py:18(quick_sort)
#   1000000    0.345    0.000    0.474    0.000 random.py:239(_randbelow_with_getrandbits)
#   1000000    0.737    0.000    1.367    0.000 random.py:292(randrange)
#   1000000    0.216    0.000    1.583    0.000 random.py:366(randint)
#   3000000    0.156    0.000    0.156    0.000 {built-in method _operator.index}
#         1    0.000    0.000    7.615    7.615 {built-in method builtins.exec}
#   1117539    0.061    0.000    0.061    0.000 {built-in method builtins.len}
#  24142788    1.343    0.000    1.343    0.000 {method 'append' of 'list' objects}
#   1000000    0.055    0.000    0.055    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1048767    0.074    0.000    0.074    0.000 {method 'getrandbits' of '_random.Random' objects}
#    558769    0.037    0.000    0.037    0.000 {method 'pop' of 'list' objects}
