F1 = open('data/F1.txt', 'w')
# print(file.read())
while True:
    text = input('Введите данные для записи в файл F1: ')
    if text == '':
        break
    F1.write(text + '\n')
F1.close()

F1 = open ('data/F1.txt', 'r')
F2 = open ('data/F2.txt', 'w')
for line in F1:
    words = line.strip().split()
    if len(words) == 1:
        F2.write(line)
F2.close()

F1 = open('data/F1.txt', 'r')
F2 = open('data/F2.txt', 'r')
ShortestWord = None
for line in F1:
    word = line.strip()
    if ShortestWord is None or len(word) < len(ShortestWord):
        ShortestWord = word

print ('Самое короткое слово из файла F2: ', ShortestWord)