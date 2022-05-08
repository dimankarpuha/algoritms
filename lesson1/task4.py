# 4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита
# они стоят, и сколько между ними находится букв.

ch1 = ord(input('Input first char:'))
ch2 = ord(input('Input second char:'))
# a = 97 place
print(f'First: {ch1-96}')
print(f'Second: {ch2-96}')


if  ch2 > ch1:
    x = ch2 - ch1 - 1
elif ch2 == ch1:
    x = 0
else:
    x = ch1 - ch2 - 1


print(x)
