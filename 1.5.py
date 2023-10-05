toy_store = {
    'Машинка': [' Пластик', 500, 10],
    'Кукла': ['Ткань', 700, 5],
    'Конструктор': ['Пластик', 1000, 3],
    'Мяч': ['Резина', 300, 20],
    'Пазл': ['Картон', 800, 7],
    'Кубики': ['Дерево', 600, 8]
}

while True:
    print('\n1. Просмотр описания')
    print('2. Просмотр цены')
    print('3. Просмотр количества')
    print('4. Всю информацию')
    print('5. Покупка')
    print('6. Выход\n')
    print('Выберите действие: ', end=' ')
    choice = input()

    if choice == '1':
        toy_name = input('\nВведите название игрушки: ')
        if toy_name in toy_store:
            print(toy_store[toy_name][0])
        else:
            print('\nТакой игрушки нет в магазине')

    elif choice == '2':
        toy_name = input('\nВведите название игрушки: ')
        if toy_name in toy_store:
            print(toy_store[toy_name][1])
        else:
            print('\nТакой игрушки нет в магазине')

    elif choice == '3':
        toy_name = input('\nВведите название игрушки: ')
        if toy_name in toy_store:
            print(toy_store[toy_name][2])
        else:
            print('\nТакой игрушки нет в магазине')

    elif choice == '4':
        print('\nИнформация о товарах в магазине:\n')
        for toy, info in toy_store.items():
            print(toy, info[0], info[1], info[2])

    elif choice == '5':
        toy_name = input('\nВведите название игрушки: ')
        if toy_name in toy_store:

            while True:
                quantity = input("Введите количество игрушек: ")
                if quantity.isdigit():
                    quantity = int(quantity)
                    break
                else:
                    print("Вы ввели неверное значение")

            if quantity <= toy_store[toy_name][2]:
                total_price = quantity * toy_store[toy_name][1]
                print('\nС вас: ', total_price, 'рублей\nОплатить?\n\n1. Да\n 2. Нет')
                while True:
                    q = input("\n\nВведите свой вариант: ")
                    if q.isdigit():
                        q = int(q)
                        if q == 1:
                            print('\n\nПокупка совершена успешно')
                        elif q == 2:
                            print('\n\nПокупка была отменена')
                        break
                    else:
                        print("Вы ввели неверное значение")
            else:
                print('\nНедостаточно товара в магазине')
        else:
            print('\nТакой игрушки нет в магазине')

    elif choice == '6':
        break

    else:
        print('\nТакой функции не существует =(')