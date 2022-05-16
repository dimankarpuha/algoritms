# 1. Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple
import random

def total_profit(firms):
    total_firms = {}
    for item in firms:
        sum_profit = item.profit1 + item.profit2 + item.profit3 + item.profit4
        total_firms[item.name] = sum_profit
    return total_firms

Firm = namedtuple('Firm', 'name, profit1, profit2, profit3, profit4')
count_firms = 10
firms = []
for item in range(count_firms):
    firms.append(Firm('firm'+str(item), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
                      random.randint(1, 10)))

total = total_profit(firms)
average_total = sum(total.values()) / len(firms)
high_average = {(key, value) for key, value in total.items() if value > average_total}
low_average = {(key, value) for key, value in total.items() if value < average_total}

print('Фирмы и их квартальный доход:', firms)
print('Фирмы и их годовой доход:', total)
print('Средний доход всех фирм:', average_total)
print('Фирмы с доходом выше среднего:', high_average)
print('Фирмы с доходом ниже среднего:', low_average)


