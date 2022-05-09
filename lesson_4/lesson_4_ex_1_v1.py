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
    min_1 = None
    min_2 = None
    for i in range_:
        if min_1 is None:
            min_1 = i
        elif i < min_1:
            min_2, min_1 = min_1, i
        elif i >= min_1 and (min_2 is None or i < min_2):
            min_2 = i
    return min_1, min_2


num_tests = 10  # количество тестов
result = []
for var in [i * 1000 for i in range(1, num_tests + 1)]:  # изменяем диапазон чисел и длину массива
    test = timeit.timeit(f"min_({var * (-1)}, {var}, {var})", number=1000, globals=globals())
    result.append(test)
    print(f'min_({var * (-1)}, {var}, {var}) - {test}')

plt.plot(result)
plt.savefig('./lesson_4_ex_1_v1_chart.jpg')

print("cProfile.run(f'min_(-1_000_000, 1_000_000, 1_000_000)')")
cProfile.run(f'min_(-1_000_000, 1_000_000, 1_000_000)')

# min_(-1000, 1000, 1000) - 0.5371370000066236
# min_(-2000, 2000, 2000) - 1.0762800000375137
# min_(-3000, 3000, 3000) - 1.662141899985727
# min_(-4000, 4000, 4000) - 2.1587056999560446
# min_(-5000, 5000, 5000) - 2.8309672999894246
# min_(-6000, 6000, 6000) - 3.3369478000095114
# min_(-7000, 7000, 7000) - 3.800164600019343
# min_(-8000, 8000, 8000) - 4.333057900017593
# min_(-9000, 9000, 9000) - 5.18126929999562
# min_(-10000, 10000, 10000) - 5.700779700011481


# cProfile.run(f'min_(-1_000_000, 1_000_000, 1_000_000)')
#          8048473 function calls in 1.880 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.007    0.007    1.880    1.880 <string>:1(<module>)
#         1    0.073    0.073    1.873    1.873 lesson_4_ex_1_v1.py:12(min_)
#         1    0.200    0.200    1.800    1.800 lesson_4_ex_1_v1.py:13(<listcomp>)
#   1000000    0.348    0.000    0.476    0.000 random.py:239(_randbelow_with_getrandbits)
#   1000000    0.744    0.000    1.377    0.000 random.py:292(randrange)
#   1000000    0.222    0.000    1.600    0.000 random.py:366(randint)
#   3000000    0.157    0.000    0.157    0.000 {built-in method _operator.index}
#         1    0.000    0.000    1.880    1.880 {built-in method builtins.exec}
#   1000000    0.055    0.000    0.055    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1048468    0.074    0.000    0.074    0.000 {method 'getrandbits' of '_random.Random' objects}
