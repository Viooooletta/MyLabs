my_diet = {'la':50,  'c':56, 'd':4, 'e':58, 'f':20}

sorted_items = sorted(my_diet.items(), key=lambda x: x[1])

for item in sorted_items[:3]:
    print(item[0], end=' ')