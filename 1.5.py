toy_store = {
    'Машинка': ['пластик', 500, 10],
    'Кукла': ['ткань', 700, 5],
    'Конструктор': ['пластик', 1000, 3],
    'Мяч': ['резина', 300, 20],
    'Пазл': ['картон', 800, 7],
    'Кубики': ['дерево', 600, 8]
}

while True:
    print('Выберите действие:')
    print('1. Просмотр описания')
    print('2. Просмотр цены')
    print('3. Просмотр количества')
    print('4. Всю информацию')
    print('5. Покупка')
    print('6. Выход')
    choice = input()

    if choice == '1':
        toy_name = input('Введите название игрушки: ')
        if toy_name in toy_store:
            print(toy_store[toy_name][0])
        else:
            print('Такой игрушки нет в магазине')

    elif choice == '2':
        toy_name = input('Введите название игрушки: ')
        if toy_name in toy_store:
            print(toy_store[toy_name][1])
        else:
            print('Такой игрушки нет в магазине')

    elif choice == '3':
        toy_name = input('Введите название игрушки: ')
        if toy_name in toy_store:
            print(toy_store[toy_name][2])
        else:
            print('Такой игрушки нет в магазине')

    elif choice == '4':
        print('Информация о товарах в магазине:')
        for toy, info in toy_store.items():
            print(toy, info[0], info[1], info[2])

    elif choice == '5':
        toy_name = input('Введите название игрушки: ')
        if toy_name in toy_store:
            quantity = int(input('Введите количество: '))
            if quantity <= toy_store[toy_name][2]:
                total_price = quantity * toy_store[toy_name][1]
                print(f'Стоимость покупки: {total_price}')
                toy_store[toy_name][2] -= quantity
                print(f'Осталось в магазине: {toy_store[toy_name][2]}')
            else:
                print('Недостаточно товара в магазине')
        else:
            print('Такой игрушки нет в магазине')

    elif choice == '6':
        break

    else:
        print('Неверный выбор')