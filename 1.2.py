string = input("Введите строку: ")

char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

max_char = max(char_count, key=char_count.get)

print('Символ, который появляется наиболее часто в веденной строке: ', max_char, '\n Введенноая строка в обратном порядке: ', string[::-1])