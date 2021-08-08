# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина начала движение")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Скорость авто: {self.speed}")

    def get_info(self):
        print(f"Модель: {self.name}; цвет: {self.color}; скорость: {self.speed}; машина полиции: {self.is_police}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости!")
        else:
            print(f"Скорость авто: {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, wanted):
        super().__init__(speed, color, name, is_police)
        self.wanted = wanted

    def is_wanted(self):
        if self.wanted is True:
            print('В розыске!')
        else:
            print('Не в розыске')

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости!")
        else:
            print(f"Скорость авто: {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


c = Car(100, "white", "BMW M5", True)
c.get_info()
c.go()
c.stop()
c.turn("right")
c.show_speed()
print(c.is_police)

wc = WorkCar(50, "black", "VAZ 2101", False, True)
wc.get_info()
wc.go()
print(wc.is_police)
wc.show_speed()
wc.is_wanted()

pc = PoliceCar(140, "blue", "porsche 911")
pc.get_info()
print(pc.is_police)
