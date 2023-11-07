class Faculty:
    def __init__(self, name):
        self.name = name
class Student(Faculty):
    def __init__(self, faculty, FullName, DataOfBirth, LastSessionResults):
        self.faculty = faculty
        self.FullName = FullName
        self.DataOfBirth = DataOfBirth
        self.LastSessionResults = LastSessionResults
    def GetInfOfStudent(self):
        print("Название Факультета: ", self.faculty.name)
        print("ФИО студента: ", self.FullName)
        print("Дата рождения студента: ", self.DataOfBirth)
        print("Последние результаты сессии: ", self.LastSessionResults)
    def SetInfOfStudent(self, FullName, DataOfBirth, LastSessionResults):
        self.FullName = FullName
        self.DataOfBirth = DataOfBirth
        self.LastSessionResults = LastSessionResults

faculty1 = Faculty("ИЭФ")
faculty2 = Faculty("ФКСИС")
faculty3 = Faculty("ФКП")
faculty4 = Faculty("ФРЭ")
faculty5 = Faculty("ФИТУ")
faculty6 = Faculty("ВФ")
faculty7 = Faculty("ФИБ")

student1 = Student(faculty1, "Каравай Виолетта Александровна", 2005, {"Логика": 7, "ОАиП": 8, "ДМ": 9, "Английский": 9})
student1.GetInfOfStudent()
print("\n")

student1.SetInfOfStudent("Каравай Глеб Александрович", 2004, {"Логика": 10, "ОАиП": 10, "ДМ": 5, "Английский": 8})
student1.GetInfOfStudent()
print("\n")

student2 = Student(faculty6, "Шкуголь Альберт Дисович", 2003, {"Логика": 5, "ОАиП": 7, "ДМ": 6, "Английский": 9})
student2.GetInfOfStudent()
print("\n")
