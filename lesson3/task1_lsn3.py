# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому # из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.
dict_value = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for num in range(2, 100):
    for key in dict_value:
        if (num % key) == 0:
            dict_value[key] += 1
print(dict_value)
