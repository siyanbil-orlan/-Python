# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def tissue_consumption(self):
        return self.v / 6.5 + 0.5

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def tissue_consumption(self):
        return 2 * self.h + 0.3

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Total:
    def __init__(self):
        self.items_ls = []

    def add_item(self, other):
        self.items_ls.append(other.tissue_consumption)

    def total_consumption(self):
        summ = 0
        for i in self.items_ls:
            summ += i
        return f"Total tissue consumption = {summ}"


c = Coat(10)
s = Suit(4)
print(c.tissue_consumption)
print(s.tissue_consumption)

# подсчет общего расхода путем сложения объектов
print(c + s)

# подсчет общего расхода через класс Total
r = Total()
r.add_item(c)
r.add_item(s)
print(r.total_consumption())
