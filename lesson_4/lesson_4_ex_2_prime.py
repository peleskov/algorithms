import timeit
import matplotlib.pyplot as plt
import cProfile


def prime(n):
    k = 0
    i = 2
    result_list = [i]
    while True:
        k += 1
        if k == n:
            break
        while True:
            i += 1
            if i > 10 and (i % 2 == 0 or i % 10 == 5):
                continue
            for j in result_list:
                if i % j == 0:
                    break
            else:
                result_list.append(i)
                break
    return i


def sieve(index):
    n_end = index
    n_start = 2
    a = [0, 0]
    while True:
        for k in range(n_start, n_end + 1):
            a.append(k)
        i = 2
        while i <= n_end:
            if a[i] != 0:
                j = i + i
                while j <= n_end:
                    a[j] = 0
                    j = j + i
            i += 1
        b = [x for x in a if x != 0]
        if len(b) >= index:
            break
        else:
            n_start = n_end + 1
            n_end = n_end * 2
    return b[index - 1]


num_tests = 10  # количество тестов
result = []
for var in [i * 1_000 for i in range(1, num_tests + 1)]:  # изменяем индекс искомого числа
    test = timeit.timeit(f"prime({var})", number=100, globals=globals())
    result.append(test)
    print(f'prime({var}) - {test}')

plt.plot(result)
plt.savefig('./lesson_4_ex_2_prime_chart.jpg')

print("cProfile.run(f'prime(10_000)'")
cProfile.run(f'prime(10_000)')


# prime(1000) - 2.3013833000004524
# prime(2000) - 8.927259599993704
# prime(3000) - 19.235005299997283
# prime(4000) - 34.29579800000647
# prime(5000) - 52.45093009999255
# prime(6000) - 68.55416920001153
# prime(7000) - 93.47470050000993
# prime(8000) - 128.0063924999995
# prime(9000) - 161.53335209999932
# prime(10000) - 190.59898599999724
# cProfile.run(f'prime(10_000)'
#          10003 function calls in 2.210 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    2.210    2.210 <string>:1(<module>)
#         1    2.209    2.209    2.210    2.210 lesson_4_ex_2_prime.py:6(prime)
#         1    0.000    0.000    2.210    2.210 {built-in method builtins.exec}
#      9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}