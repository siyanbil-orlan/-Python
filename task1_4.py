# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

n = int(input('Enter a number: '))
max_i = 0

while n > 10:
    i = n % 10
    n //= 10
    if i > max_i:
        max_i = i
else:
    if n > max_i:
        max_i = n

print(max_i)
