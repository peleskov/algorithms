"""
    Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
    Программа должна вычислять сумму введенных элементов каждой строки
    и записывать ее в последнюю ячейку строки.
    В конце следует вывести полученную матрицу.
"""
rows = 5
cols = 4

matrix = []
for _ in range(0, rows):
    row = [int(i) for i in (input(f'Введите {cols - 1} {"числа" if 2 <= (cols - 1) <= 4 else "чисел"} через пробел: ')).split()]
    sum_row = 0
    for s in row:
        sum_row += s
    row.append(sum_row)
    matrix.append(row)

for row in matrix:
    for i in row:
        print(f'{i:>4}', end='')
    print('')
