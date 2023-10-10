def find_positive_line():
    for r in matrix:
        if all(row > 0 for row in r):
            print("Сумма первой положительной строки в матрице: ", sum(r))
            break
    if sum(r) == 0:
        print("В данной матрице нет ни одной полностью положительной строки")

matrix = []
print('Введите размерность матрицы n x m')
while True:
    try:
        n = int(input("\nВведите значение n: "))
        m = int(input("\nВведите значение m: "))
        if n >= 0 and m >= 0:
            break
        else:
            print('\nЗначения n и m должны быть положительными!')
    except ValueError:
        print("\nВы ввели неверное значение!")
for i in range(n):
    row = []
    for j in range(m):
        while True:
            try:
                element = float(input('\nВведите элемент матрицы ' + str(i+1) + '-ой строки и ' + str(j+1) + '-ого столбца: '))
                row.append(element)
                break
            except ValueError:
                print('\nЭлемент матрицы должен быть числовым!')
    matrix.append(row)

print('\nВведенная матрица:')
for row in matrix:
    print(row)

find_positive_line()