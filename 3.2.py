MyCity = input('Введите пункт назначения: ')
file = open('data/Вокзал.txt', 'r', encoding='utf-8')
AllTransportInf = file.readlines()
find = 0
SuitableTransports = []
print('Это все билеты, которые стоят меньше 50 рублей:')

for line in AllTransportInf:
    TrainNum, city, day, time, price = line.split()

    if MyCity == city:
       find = 1
       SuitableTransports.append((TrainNum, city, day, time, price))


    if int(price) < 50:
        print(TrainNum, city, day, time, price)
if find == 1:
    print('\nВсе рейсы в город', MyCity, ":")
    for result in SuitableTransports:
        print(result[0], result[2], result[3], result[4])
elif find == 0:
    print('\nК сожаленью по вашему запросу рейсов не найдено')


file.close()