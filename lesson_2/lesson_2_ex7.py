"""
7.  Напишите программу, доказывающую или проверяющую,
    что для множества натуральных чисел выполняется равенство:
    1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""
n = int(input('Введите натуральное число: '))

b = 0
c = n * (n + 1) / 2
for i in range(1, n+1):
    b += i

if b == c:
    print(f'{b} = {c}')
else:
    print(f'{b} != {c}')