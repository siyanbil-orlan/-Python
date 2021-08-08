# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

filename = 'employee_salary.txt'
with open(filename, 'r') as f:
    em_numb = 0
    sal_sum = 0
    for line in f:
        ls = line.split()
        if int(ls[1]) < 20000:
            print("Оклад менее 20000: ", ls[0])
        sal_sum += int(ls[1])
        em_numb += 1
    average_salary = sal_sum / em_numb
    print(f"Средняя величина дохода сотрудников: {average_salary}")
