while True:
    try:
        number = int(input("Введите целое число: "))
    except ValueError:
        print("Вы ввели неверное значение!")
    else:
        print("Вы ввели число")
    finally:
        print("Вы что-то ввели")
        break