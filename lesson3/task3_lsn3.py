# 3. В массиве случайных целых чисел
# поменять местами минимальный и максимальный элементы.
import random

arr = [random.randint(1, 100) for i in range(10)]
print('Исходный массив:', arr)

max_el = max(arr)
min_el = min(arr)
print(f'max:{max_el}, min:{min_el}')

arr[arr.index(max_el)], arr[arr.index(min_el)] = arr[arr.index(min_el)], arr[arr.index(max_el)]
print('Массив с измененными элементами', arr)
