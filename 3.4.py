import json

file = open('data/Данные о фирме.txt', 'r', encoding='utf-8')

lines = file.readlines()

profits = {}

TotalProfit = 0
count = 0
for line in lines:
    values = line.split()
    if len(values) == 4:
        name, ownership, revenue, costs = values
        profits = int(revenue) - int(costs)
        profits[name] = profit
        if profit > 0:
            TotalProfit += profit
            count += 1
AvarageProfit = TotalProfit / count if count > 0 else 0
file.close()

file = open('data/Данные о фирме.txt', 'w', encoding='utf-8')
json.dump(AvarageProfit, file)
file.close()