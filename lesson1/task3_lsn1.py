# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
import random

a = int(input('Input first num:'))
b = int(input('Input second num:'))
num1 = random.randint(a, b)
print(num1)

a = int(input('Input first num:'))
b = int(input('Input second num:'))
num2 = random.uniform(a,b)
print(num2)

a = ord(input('Input first char:'))
b = ord(input('Input second char:'))
char1 = chr(random.randint(a, b))
print(char1)


