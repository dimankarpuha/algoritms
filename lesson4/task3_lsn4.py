# 3. В массиве случайных целых чисел
# поменять местами минимальный и максимальный элементы.
import random
import cProfile

def reverse_num(arr):
    max_el = arr[0]
    max_position = 0
    min_el = arr[0]
    min_position = 0
    for position, el in enumerate(arr):
        if el > max_el:
            max_el = el
            max_position = position
        elif el < min_el:
            min_el = el
            min_position = position
    temp = arr[max_position]
    arr[max_position] = arr[min_position]
    arr[min_position] = temp


def main():
    arr = [random.randint(1, 100) for i in range(100000)]
    reverse_num(arr)

#main()

#100 loops, best of 5: 32.8 nsec per loop
# 1000 loops, best of 5: 16.6 nsec per loop
cProfile.run('main()')