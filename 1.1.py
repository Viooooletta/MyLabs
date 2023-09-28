# Вывести на экран 51 простое число
primeNumber = 2
counter = 0

print('51 простое число: ')

while counter <= 51:
    denominator = 2
    n = 0

    while denominator <= primeNumber / 2:

        if primeNumber % denominator != 0:
            denominator += 1
        else:
            n = 1
            break

    if n == 0:
        counter += 1
        print(primeNumber, end=" ")
        primeNumber += 1
    elif n == 1:
        primeNumber += 1