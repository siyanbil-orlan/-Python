# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    _income = {"wage": 1000, "bonus": 100}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        # self._income = {"wage": 1000, "bonus": 100}


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return f"Полное имя сотрудника: {self.surname} {self.name}"

    def get_total_income(self):
        result = self._income["wage"] + self._income["bonus"]
        return result


w = Position("Orlan", "Siyabil", "librarian")
print(w.get_full_name())
print(w.get_total_income())
