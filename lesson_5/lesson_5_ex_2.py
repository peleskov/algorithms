from copy import copy
from collections import deque


def hex_dec(num, to='dec'):
    if to == 'dec':
        number = 0
        i = len(num) - 1
        for n in num:
            number += (ALFA.index(n) + 10 if n in ALFA else int(n)) * (16 ** i)
            i -= 1
    else:
        number = deque()
        rest = num % 16
        int_ = num // 16
        while int_ > 16:
            if rest >= 10:
                number.appendleft(ALFA[rest - 10])
            else:
                number.appendleft(str(rest))
            rest = int_ % 16
            int_ = int_ // 16
        if rest >= 10:
            number.appendleft(ALFA[rest - 10])
        else:
            number.appendleft(str(rest))
        if int_ > 0:
            if int_ >= 10:
                number.appendleft(ALFA[int_ - 10])
            else:
                number.appendleft(str(int_))
    return number


def my_sum(*args):
    nums_list = [copy(arg) for arg in args]
    output = deque()
    result = deque()
    while True:
        nums_pop = [nums.pop() for nums in nums_list if nums]
        if not nums_pop:
            break
        sum_ = 0
        for n in nums_pop:
            sum_ += ALFA.index(n) + 10 if n in ALFA else int(n)
        result = hex_dec(sum_, 'hex')
        output.appendleft(result.pop())
        if nums_list:
            nums_list.append(result)
    while len(result) > 0:
        output.appendleft(result.pop())
    return output


def my_mult(*args):
    nums_list = [hex_dec(copy(arg)) for arg in args]
    result = 1
    for num in nums_list:
        result *= num
    return hex_dec(result, 'hex')


ALFA = 'A', 'B', 'C', 'D', 'E', 'F'
num_1 = deque(map(str, input('Введите 1 число в шестнадцатиречной системе: ').upper()))
num_2 = deque(map(str, input('Введите 2 число в шестнадцатиречной системе: ').upper()))
print(my_sum(num_1, num_2))  # Сумма любого количества чисел
print(my_mult(num_1, num_2))  # Произведение любого количества чисел

