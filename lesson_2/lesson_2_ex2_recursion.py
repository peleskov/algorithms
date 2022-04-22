"""
2.  Посчитать четные и нечетные цифры введенного натурального числа.
    Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def calc(num, div=10, odd=0, even=0, dig_odd='', dig_even=''):
    dig = int((num % div) // (div / 10))
    if dig % 2 != 0:
        if dig_odd != '':
            dig_odd += ', '
        dig_odd += f'{dig}'
        odd += 1
    else:
        if dig_even != '':
            dig_even += ', '
        dig_even += f'{dig}'
        even += 1
    if num == num % div:
        return f'Число {a} содержит {even} четных цифры ({dig_even}) и {odd} нечетных цифры ({dig_odd})'
    else:
        return calc(num, div * 10, odd, even, dig_odd, dig_even)


a = int(input('Введите натуральное число: '))
print(calc(a))
