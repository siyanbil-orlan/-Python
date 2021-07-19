# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные
# числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

ls = [el for el in range(100, 1001) if el % 2 == 0]
print(ls)


def composition(first_param, second_param):
    return first_param * second_param


result = reduce(composition, ls)
print(result)
