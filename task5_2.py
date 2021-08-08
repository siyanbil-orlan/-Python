# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

filename = 'test_file.txt'
with open(filename, 'r') as f:
    str_count = 0
    for line in f:
        str_count += 1
        word_count = len(line.split())
        print(f'Количество слов в {str_count} строке: ', word_count)

print(f'Колиество строк в файле {filename}: ', str_count)
