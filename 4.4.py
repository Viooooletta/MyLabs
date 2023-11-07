class Animal:
    total_animals = 0
    def __init__(self, species, age):
        self.species = species
        self.age = age
        Animal.total_animals += 1
    def description(self):
        print("Это", self.species)
        print("Ему", self.age, "Лет")
    @staticmethod
    def animal_sound(sound):
        print("Животное издает звук:", sound)
    @classmethod
    def get_total_animals(cls):
        print("Всего в зоопарке находится: ", cls.total_animals, "животных", end="\n\n")

lion = Animal("Лев", 5)
lion.description()
Animal.animal_sound("р-р-а-а-р")
Animal.get_total_animals()

monkey = Animal("Обезьяна", 12)
monkey.description()
Animal.animal_sound("у-а-а-у-а-а")
Animal.get_total_animals()

parrot = Animal("Попугай ара", 3)
parrot.description()
Animal.animal_sound("Гоша хороший")
Animal.get_total_animals()


