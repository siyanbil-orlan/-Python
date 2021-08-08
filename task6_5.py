# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("drawing")


class Pen(Stationery):
    def draw(self):
        print(self.title, "drawing")


class Pencil(Stationery):
    def draw(self):
        print(self.title, "drawing")


class Handle(Stationery):
    def draw(self):
        print(self.title, "drawing")


p = Pen("Pen")
p.draw()

pc = Pencil("Pencil")
pc.draw()

h = Handle("Handle")
h.draw()
