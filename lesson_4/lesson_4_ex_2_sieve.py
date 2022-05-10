import timeit
import matplotlib.pyplot as plt
import cProfile


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
    test = timeit.timeit(f"sieve({var})", number=100, globals=globals())
    result.append(test)
    print(f'sieve({var}) - {test}')

plt.plot(result)
plt.savefig('./lesson_4_ex_2_sieve_chart.jpg')

print("cProfile.run(f'sieve(10_000)'")
cProfile.run(f'sieve(10_000)')


# sieve(1000) - 0.354743400006555
# sieve(2000) - 1.5954659999988507
# sieve(3000) - 2.2755633000051603
# sieve(4000) - 3.0938098000042373
# sieve(5000) - 3.9886113999964437
# sieve(6000) - 4.807548400000087
# sieve(7000) - 5.524040499993134
# sieve(8000) - 6.313198399991961
# sieve(9000) - 6.950804599997355
# sieve(10000) - 8.085351100002299
# cProfile.run(f'sieve(10_000)'
#          160013 function calls in 0.115 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.115    0.115 <string>:1(<module>)
#         5    0.007    0.001    0.007    0.001 lesson_4_ex_2_sieve.py:21(<listcomp>)
#         1    0.095    0.095    0.114    0.114 lesson_4_ex_2_sieve.py:6(sieve)
#         1    0.000    0.000    0.115    0.115 {built-in method builtins.exec}
#         5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    159999    0.011    0.000    0.011    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
