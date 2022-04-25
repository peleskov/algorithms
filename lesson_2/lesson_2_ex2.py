"""
2.  Посчитать четные и нечетные цифры введенного натурального числа.
    Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
a = int(input('Введите натуральное число: '))
div = 10
odd = 0
even = 0
dig_even = ''
dig_odd = ''
while True:
    dig = int((a%div)//(div/10))
    if dig%2 != 0:
        if dig_odd != '':
            dig_odd += ', '
        dig_odd += f'{dig}'
        odd += 1
    else:
        if dig_even != '':
            dig_even += ', '
        dig_even += f'{dig}'
        even += 1
    if a == a%div:
        break
    div = div * 10
print(f'Число {a} содержит {even} четных цифры ({dig_even}) и {odd} нечетных цифры ({dig_odd})')