# 3. В массиве случайных целых чисел
# поменять местами минимальный и максимальный элементы.
import random
import cProfile

def reverse_num(arr):
    max_el = arr[0]
    min_el = arr[0]
    for el in arr:
        if el > max_el:
            max_el = el
        elif el < min_el:
            min_el = el
    arr[arr.index(max_el)], arr[arr.index(min_el)] = arr[arr.index(min_el)], arr[arr.index(max_el)]

def main():
    arr = [random.randint(1, 100) for i in range(100000)]
    reverse_num(arr)

#main()

#10 loops, best of 5: 147 nsec per loop
#100 loops, best of 5: 32.8 nsec per loop
# 1000 loops, best of 5: 16.6 nsec per loop
cProfile.run('main()')