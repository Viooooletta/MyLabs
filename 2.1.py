def rank_determine():
    while True:
        try:
            number = int(input("Введите целое число, я посчитаю количество его разрядов: "))
            if number < 0:
                number *= -1
            break
        except ValueError:
            print("\nВы ввели неверное значение!\n")
    rank = 0
    while number != 0:
        rank += 1
        number //= 10
    print('Количество разрядов: ', rank)

rank_determine()

