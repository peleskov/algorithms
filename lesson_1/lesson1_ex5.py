"""
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

s1, s2 = map(str, input('Введите две буквы a-z, через пробел: ').split())

pos_s1 = ord(s1) - 96
pos_s2 = ord(s2) - 96
qty = pos_s2 - pos_s1 - 1

print(f'Позиция букв в алфавите {pos_s1} {pos_s2}', f'между буквами {qty} букв', sep='\n')
