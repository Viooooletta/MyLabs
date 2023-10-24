file = open('data/Предметы.txt', 'r', encoding='utf-8')

lines = file.readlines()

SubjectsList = {}

for line in lines:
    subjects, lessons = line.split(':')
    subjects = subjects.strip()
    lessons = lessons.strip()
    lessons = lessons.split()
    AllLessons = []
    for i in lessons:
        if i.isdigit():
            AllLessons.append(int(i))
    SubjectsList[subjects] = AllLessons
print(SubjectsList)

file.close()