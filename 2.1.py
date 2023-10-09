def rankDetermine():
    while True:
        number = input("Введите число, я посчитаю количество его разрядов: ")
        if number.isdigit():
            number = int(number)
            break
        else:
            print("Вы ввели неверное значение! Число должно быть целым")
    rank = 0
    while number > 0:
        rank += 1
        number //= 10
    print('Количество разрядов: ', rank)


rankDetermine()

