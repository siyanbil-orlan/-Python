# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом
# английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

numbs = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}

with open('new_numbers.txt', 'x') as g:
    with open('numbers.txt', 'r') as f:
        for line in f:
            for key in numbs.keys():
                if key in line:
                    new_line = line.replace(key, numbs[key])
                    g.write(new_line)
