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
    range_sorted = sorted(range_)
    return range_sorted[:2]


num_tests = 10  # количество тестов
result = []
for var in [i * 1000 for i in range(1, num_tests + 1)]:  # изменяем диапазон чисел и длину массива
    test = timeit.timeit(f"min_({var * (-1)}, {var}, {var})", number=1000, globals=globals())
    result.append(test)
    print(f'min_({var * (-1)}, {var}, {var}) - {test}')

plt.plot(result)
plt.savefig('./lesson_4_ex_1_v3_chart.jpg')

print("cProfile.run(f'min_(-1_000_000, 1_000_000, 1_000_000)')")
cProfile.run(f'min_(-1_000_000, 1_000_000, 1_000_000)')

# min_(-1000, 1000, 1000) - 0.5538517000386491
# min_(-2000, 2000, 2000) - 1.1054425000329502
# min_(-3000, 3000, 3000) - 1.7196660000481643
# min_(-4000, 4000, 4000) - 2.235179600014817
# min_(-5000, 5000, 5000) - 2.961620200017933
# min_(-6000, 6000, 6000) - 3.4728807999636047
# min_(-7000, 7000, 7000) - 4.047356499999296
# min_(-8000, 8000, 8000) - 4.5958288999972865
# min_(-9000, 9000, 9000) - 5.520084500021767
# min_(-10000, 10000, 10000) - 6.104738200025167


# cProfile.run(f'min_(-1_000_000, 1_000_000, 1_000_000)')
#          8049056 function calls in 2.072 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.031    0.031    2.072    2.072 <string>:1(<module>)
#         1    0.000    0.000    2.041    2.041 lesson_4_ex_1_v3.py:12(min_)
#         1    0.208    0.208    1.841    1.841 lesson_4_ex_1_v3.py:13(<listcomp>)
#   1000000    0.358    0.000    0.490    0.000 random.py:239(_randbelow_with_getrandbits)
#   1000000    0.754    0.000    1.405    0.000 random.py:292(randrange)
#   1000000    0.227    0.000    1.632    0.000 random.py:366(randint)
#   3000000    0.162    0.000    0.162    0.000 {built-in method _operator.index}
#         1    0.000    0.000    2.072    2.072 {built-in method builtins.exec}
#         1    0.201    0.201    0.201    0.201 {built-in method builtins.sorted}
#   1000000    0.057    0.000    0.057    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1049050    0.075    0.000    0.075    0.000 {method 'getrandbits' of '_random.Random' objects}
