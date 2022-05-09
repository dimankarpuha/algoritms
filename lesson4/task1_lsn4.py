# 3. В массиве случайных целых чисел
# поменять местами минимальный и максимальный элементы.
import random
import cProfile

def reverse_num(arr):
    max_el = max(arr)
    min_el = min(arr)
    arr[arr.index(max_el)], arr[arr.index(min_el)] = arr[arr.index(min_el)], arr[arr.index(max_el)]

def main():
    arr = [random.randint(1, 100) for i in range(100000)]
    reverse_num(arr)

main()

#10 loops, best of 5: 147 nsec per loop
#100 loops, best of 5: 28.6 nsec per loop
# 1000 loops, best of 5: 18.4 nsec per loop
#cProfile.run('main()')


