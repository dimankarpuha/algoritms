# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или
# меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.
import random
num = random.randint(0, 100)
for i in range(1, 11):
    print('Try #', i)
    num_of_user = int(input('Введите число:'))
    if num_of_user < num:
        print('Number low')
    elif num_of_user > num:
        print('Number high')
    else:
        print('Correct! ', num)
        break

