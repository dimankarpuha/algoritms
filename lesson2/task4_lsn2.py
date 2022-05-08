# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите число n:'))
sum_elements = 0
num = 1
for i in range(n):
    print(num)
    sum_elements += num
    num /= -2

print(f'Сумма элементов {sum_elements}')