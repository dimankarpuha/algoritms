# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random
arr = [random.randint(-50, 50) for i in range(10)]
print(arr)

position = 0
max_in_min = arr[position]
for i in range(len(arr)):
    if (arr[i] < 0) and (arr[i] > max_in_min):
        max_in_min = arr[i]
        position = i

print(f'max from negative: {max_in_min}, position:{position}')




