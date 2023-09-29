list = [13, 56, 'Python', 34.19, 'love']
for i in range(len(list)):
    if type(list[i]) == int:
        if list[i] % 2 == 0:
            digits_product = 1
            for digit in str(list[i]):
                digits_product *= int(digit)
            list[i] = digits_product
        else:
            list[i] = 1
print(list)