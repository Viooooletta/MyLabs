# def found_positive_line():
#       rank = 0
#     while number > 0:
#         rank += 1
#         number //= 10
#     print('Количество разрядов: ', rank)
#
while True:
    n = input("Введите размерность матрицы n x m\n\nВведите значение n: ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Вы ввели неверное значение! Число должно быть целым ")



