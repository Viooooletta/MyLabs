import json

file = open('data/Данне о фирме.txt', 'r', encoding='utf-8')

lines = file.readlines()

profits = {}

TotalProfit = 0
count = 0
for line in lines:
    name, OwnerShip, revenue, costs = line.split()
    revenue = int(revenue)
    costs = int(costs)
    profit = revenue - costs
    profits[name] = profit
    if profit > 0:
        TotalProfit += profit
        count += 1
result = [profits, {'AvarageProfit': TotalProfit / count}]

file.close()

file = open('data/Данные о фирме.txt', 'w', encoding='utf-8')
json.dump(result, file)