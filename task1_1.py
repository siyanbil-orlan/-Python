# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = input("Enter your name: ")
print(f'hello, {name}!')

age = int(input("How old are you?: "))
if age > 17:
    print('Ok')
else:
    print('Not now')
