# 2. По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
x1 = int(input('введите x1:'))
y1 = int(input('введите y1:'))
x2 = int(input('введите x2:'))
y2 = int(input('введите y2:'))

# y1 = k*x1 + b
# k = (y2-y1)/(x2-x1)
# b = y1 - k*x1
# y2 = k*x2 +b
if x1 != x2:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - (k*x1)
    if b > 0:
        print(f'y = {k}x+{b}')
    elif b == 0:
        print(f'y = {k}x')
    else:
        print(f'y = {k}x{b}')
else:
    print(f'при х1=х2, уравнение х={x1}')

