# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться
# сортировка пузырьком. Улучшенные версии сортировки,
# например, расчёской, шейкерная и другие в зачёт не идут.

# В функцию buble_v2 добавил переменную not_sorted, она нужна для выхода из цикла,
# когда цикл уже отсортирован. При этом обычная пузырьковая сортировка будет продолжать
# работать, даже если массив уже отсортирован. На полностью рандомном массиве выигрыш был до 300 итераций
# Кол-во проходов v1: 20100
# Кол-во проходов v2: 19800
# если массив наполовину отсортирован то выигрыш в почти в два раза
# Кол-во проходов v1: 20100
# Кол-во проходов v2: 12474

import random

def bubble_v1(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            count += 1
        count += 1
    return count

def bubble_v2(array):
    count = 0
    for i in range(len(array)):
        not_sorted = True
        for j in range(len(array)-i-1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                not_sorted = False
            count += 1
        count += 1
        if not_sorted:
            break
    return count

array_1 = [n for n in range(-100, 100)]
random.shuffle(array_1)
array_2 = array_1.copy()

print('Исходный массив:', array_1)
print('Кол-во проходов v1:',bubble_v1(array_1))
print('Отсортированый массив по v1',array_1)

print('Исходный массив:', array_2)
print('Кол-во проходов v2:', bubble_v2(array_2))
print('Отсортированый массив по v2', array_2)

# делаем массив наполовину отсортированым
array = [n for n in range(100, -100, -1)]
first_part_array = array[:len(array)//2]
second_part_array = array[len(array)//2:]
random.shuffle(second_part_array)
first_part_array.extend(second_part_array)
array_copy = first_part_array.copy()

print('********************* наполовину отсортированный массив ***************************')
print('Исходный массив :', first_part_array)
print('Кол-во проходов v1:',bubble_v1(first_part_array))
print('Отсортированый массив по v1',first_part_array)

print('Исходный массив:', array_copy)
print('Кол-во проходов v2:', bubble_v2(array_copy))
print('Отсортированый массив по v2', array_copy)





