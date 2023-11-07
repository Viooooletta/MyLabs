class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print("Машина едет")
    def stop(self):
        print("Машина остановилась")
    def turn(self, direction):
        print("Машина повернула", direction)

    def show_speed(self):
        if (self.speed > 0):
            self.go()
            print("со скоростью", self.speed, "км/ч")
        else:
            self.stop()

class TownCar(Car):
    def show_speed_town_car(self):
        self.show_speed()
        if self.speed > 60:
            print("Внимание!", self.color, self.name, "превысил скорость на ", self.speed - 60, "км/ч")

class SpotCar(Car):
    def show_speed_sport_car (self):
        self.show_speed()

class WorkCar(Car):
    def show_speed_work_car(self):
        self.show_speed()
        if self.speed > 40:
            print("Внимание!", self.color, self.name, "превысил скорость на ", self.speed - 60, "км/ч")

class PoliceCar(Car):
    def show_speed_police_car(self):
        self.show_speed()

town_car = TownCar(0,"Красная", "Toyota", "Нет")
town_car.show_speed_town_car()
print("\n")

work_car = WorkCar(80,"Черный", "Ford", "Нет")
work_car.show_speed_work_car()
print("\n")

police_car = PoliceCar(90,"Белый", "Dodge", "Да")
police_car.show_speed_police_car()
print("\n")