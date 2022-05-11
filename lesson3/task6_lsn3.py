# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

arr = [random.randint(-10, 10) for i in range(10)]
print(arr)

max_position = arr.index(max(arr))
min_position = arr.index(min(arr))

summ = sum(arr[min_position+1:max_position]) if min_position < max_position else sum(arr[max_position+1:min_position])
print(f'max:{arr[max_position]},position: {max_position}')
print(f'min:{arr[min_position]},position: {min_position}')
print(summ)

