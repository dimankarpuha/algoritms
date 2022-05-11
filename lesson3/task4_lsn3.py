# 4. Определить, какое число в массиве встречается чаще всего.
import random

arr = [random.randint(1, 5) for i in range(50)]
print('Исходный массив:', arr)

dict_value = {}

for el in arr:
    dict_value[el] = dict_value.setdefault(el, 0) + 1

print(dict_value)

max_num = 0
key_max = 0
for key in dict_value:
    if dict_value[key] > max_num:
        max_num = dict_value[key]
        key_max = key

print('Чаще всего попадается число:', key_max)
