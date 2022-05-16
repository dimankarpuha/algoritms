# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(),
# sha1() или любой другой из модуля hashlib задача считается не решённой.
import hashlib

def count_substrings(s):
    sub_strings = []
    # формируем подстроки в список
    for i in range(2, len(s)):
        for j in range(0, len(s) - i + 1):
            sub_strings.append(s[j:j+i])
    print(sub_strings)
    # используем множество (т.к. если будут одинаковые хэши множество их удалит
    hash_set = set()
    #проходим по списку подстрок, хэшируем их и заносим в множество
    for item in sub_strings:
        hash_set.add(hashlib.sha1(item.encode('UTF-8')).hexdigest())
    print('Всего кол-во подстрок:', len(sub_strings))
    print('Количество разных подстрок', len(hash_set))


str_for_hash = 'strstr'
count_substrings(str_for_hash)



