"""
8.  Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
    Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def calc(dig, num):
    q = 0
    div = 10
    while True:
        if int((num%div)//(div/10)) == dig:
            q += 1
        if num == num%div:
            break
        div = div * 10
    return q


n = int(input('Из скольки цифр будет последовательность: '))
a = int(input('Введите искомое натуральное число: '))
qty = 0;
sequence = ''
for i in range(1, n+1):
    b = int(input(f'Введите натуральное число N {i}: '))
    sequence = f'{b}' if sequence == '' else f'{sequence}, {b}'
    qty += calc(a, b)

print(f'В введенной последовательности ({sequence}) число {a} встречается {qty} {"раз" if 5 < qty > 1 else "раза"}')
