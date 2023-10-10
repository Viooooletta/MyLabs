def get_unique_repeated_numbers(numbers):
    repeated_numbers = []
    for number in numbers:
        if numbers.count(number) == 2 and number not in repeated_numbers:
            repeated_numbers.append(number)
    return repeated_numbers

def process_input(input_data):
    if type(input_data) == list:
        max_index = input_data.index(max(input_data))
        min_index = input_data.index(min(input_data))
        input_data[max_index], input_data[min_index] = input_data[min_index], input_data[max_index]
        print("Список, где максимальный и минимальный элементы поменялись местами:", input_data)
        unique_repeated_numbers = get_unique_repeated_numbers(input_data)
        print("\nУникальные повторяющиеся числа в списке:", unique_repeated_numbers)
    elif type(input_data) == dict:
        keys = list(input_data.keys())
        print("\nКлючи словаря:", keys)
        min_key = min(input_data, key=input_data.get)
        print("\nКлюч с минимальным значением:", min_key)
    elif type(input_data) == int:
        if input_data < 2:
            print("\nЧисло не является простым")
            return
        for i in range(2, int(input_data/2)+1):
            if input_data % i == 0:
                print("\nЧисло не является простым")
                return
        print("\nЧисло является простым")
    elif type(input_data) == str:
        sum = 0
        for char in input_data:
            if char.isdigit():
                sum += int(char)
        print("\nСумма чисел в строке:", sum)
    else:
        print("\nТип данных не поддерживается")

input_data = [1, 2, 3, 4, 5, 5, 6, 6]
process_input(input_data)

input_data = {'a': 1, 'b': 2, 'c': -1, 'd': 3}
process_input(input_data)

input_data = 7
process_input(input_data)

input_data = "abc123"
process_input(input_data)