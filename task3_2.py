# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def get_person(name, surname, birth='', city='', email='', number=''):
    print(name, surname, birth, city, email, number)


get_person('orlan', surname='siyanbil', birth='06.04.1993', email='siyanbil.orlan@gmail.com')
