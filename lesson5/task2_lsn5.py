# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque
dec_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
           10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
hex_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, }
def hex_in_dec(arr_num):
    num = 0
    for position, el in enumerate(arr_num):
        num += hex_dec[el]*(16**position)
    return num
def dec_in_hex(num):
    hex = deque()
    while num > 16:
        hex.appendleft(dec_hex[num % 16])
        num //= 16
    hex.appendleft(dec_hex[num % 16])
    return hex

num1_input = 'A2'
num2_input = 'C4F'

arr_num1 = [el for el in num1_input[::-1]]
arr_num2 = [el for el in num2_input[::-1]]
num1_dec = hex_in_dec(arr_num1)
num2_dec = hex_in_dec(arr_num2)
sum_dec = num1_dec + num2_dec
mult_dec = num1_dec * num2_dec

print(f'Number1:{arr_num1}, dec:{num1_dec}')
print(f'Number2:{arr_num2}, dec:{num2_dec}')
print(f'Summa:{dec_in_hex(sum_dec)}')
print(f'Mult:{dec_in_hex(mult_dec)}')

