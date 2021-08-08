# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('numbers_count.txt', 'w+') as f:
    f.write(input('Введите числа через пробел: '))
    f.seek(0)
    content = f.read()
    cont_ls = list(map(int, content.split()))
    s = 0
    for i in cont_ls:
        s += i
    print(s)
