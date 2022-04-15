a = int(input('Введите трехзначное число: '))

a3 = int(a % 10)
a2 = int((a % 100 - a3) / 10)
a1 = int((a - a3 - a2 * 10) / 100)

sum = a1 + a2 + a3
mul = a1 * a2 * a3

print(f'Сумма цифр: {sum}')
print(f'Произведение цифр: {mul}')