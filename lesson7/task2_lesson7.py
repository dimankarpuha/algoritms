# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random


def merge_sort(array_list):
    if len(array_list) > 1:
        mid = len(array_list) // 2  # делим на две части
        left = merge_sort(array_list[:mid])  # рекурсия на левую
        right = merge_sort(array_list[mid:])
        i = j = 0
        result = []
        while i < len(left) and j < len(right):  # записываем в резальт пока не дойдем до конца i или j
            if left[i] < right[j]:  # если лев меньше прав добавляем лев в резальт
                result.append(left[i])
                i += 1
            else:
                result.append(right[j]) # если прав меньше лев добавл прав в резальт
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result
    else:
        return array_list  # возвращаем список с одним элементом, когда функция разбила уже до минимального эл-та


max_count = 10
array = [random.uniform(0, 50) for _ in range(max_count)]
random.shuffle(array)
print('unsorted', array)
print('_sorted_', merge_sort(array))
