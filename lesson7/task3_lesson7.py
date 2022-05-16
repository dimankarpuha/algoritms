# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).
import random

def quicksort_v2(nums):
    if len(nums) <= 1:
        return nums
    pivot = random.choice(nums)
    left = list(filter(lambda x: x < pivot, nums))
    center = [i for i in nums if i == pivot]
    right = list(filter(lambda x: x > pivot, nums))
    return quicksort_v2(left) + center + quicksort_v2(right)


m = 10
size_array = 2 * m + 1
array = [n for n in range(size_array)]
random.shuffle(array)
print(array)
array = quicksort_v2(array)
mediana = array[len(array) // 2]
left = array[:mediana]
right = array[mediana+1:]
print(left, mediana, right)

#new_array = deque(array[0])
#Возьмём представленный ниже список. Мы хотим найти медиану.
