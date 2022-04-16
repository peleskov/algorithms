"""
Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число,
    случайное вещественное число,
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random

start, end = map(int, input('Введите два числа, через пробел: ').split())

result = random.randint(start, end)

print(result)

start, end = map(float, input('Введите двa вещественных числа, через пробел: ').split())

result = random.uniform(start, end)

print(result)

start, end = map(str, input('Введите две буквы a-z, через пробел: ').split())

result = random.randint(ord(start), ord(end))

print(chr(result))
