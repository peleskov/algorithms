"""
9.  Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
    Вывести на экран это число и сумму его цифр.
"""


def calc(a):
    dig_sum = 0
    div = 10
    while True:
        dig_sum += int((a % div) // (div / 10))
        if a == a % div:
            break
        div = div * 10
    return dig_sum


max_sum = 0
dig = 0
sequence = ''
while True:
    in_a = int(input('Введите натуральное число: '))
    if in_a != 0:
        sequence = f'{in_a}' if sequence == '' else f'{sequence}, {in_a}'
        cur_sum = calc(in_a)
        if cur_sum > max_sum:
            max_sum = cur_sum
            dig = in_a
    else:
        break

print(f'В введенной последовательности ({sequence}) первое встреченное число с наибольшой суммой цифр = {max_sum}, это число {dig}')
