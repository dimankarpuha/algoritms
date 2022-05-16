# размер массива при разных типах данных
# сравним списки, множества и кортежи
# вывод меньше всего занимает кортеж, но с ним ничего сделать нельзя
# большн всего места в памяти занимает множество
import sys

def getsize(objects):
    lst_objects = {}
    for el in objects:
        lst_objects[type(el)] = sys.getsizeof(el)
    return lst_objects

# print(sys.version) 3.10.4 (main, Apr  2 2022, 09:04:19) [GCC 11.2.0]
#print(sys.platform) linux
arr_lst = [x for x in range(10000)]
#<class 'list'>: 85176,

arr_set = {x for x in range(10000)}
#  <class 'set'>: 524504,

arr_tuple = tuple([x for x in range(10000)])
#  <class 'tuple'>: 80040

print(arr_lst)
print(arr_set)
print(arr_tuple)

print(getsize([arr_lst, arr_set, arr_tuple]))
