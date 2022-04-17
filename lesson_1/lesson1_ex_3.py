x1, y1 = map(int, input('Введите координаты первой точки, через пробел: ').split())
x2, y2 = map(int, input('Введите координаты второй точки, через пробел: ').split())

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f'y = {round(k, 3)} * x {"+" if b > 0 else "-"} {round(abs(b), 3)}')
