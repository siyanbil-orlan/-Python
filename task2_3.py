# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

# по-колхозному через list
n = int(input('Enter the month number: '))

season_ls = ['spring', 'summer', 'autumn', 'winter']

if 3 <= n <= 5:
    print(season_ls[0])
elif 6 <= n <= 8:
    print(season_ls[1])
elif 9 <= n <= 11:
    print(season_ls[2])
elif n == 12 or n < 3:
    print(season_ls[3])
else:
    print('Check the number of months in a year!')


# через dict
n = int(input('Enter the month number: '))

season_dict = {
    (3, 4, 5): 'spring', (6, 7, 8): 'summer', (9, 10, 11): 'autumn', (1, 2, 12): 'winter'
}

for key in season_dict.keys():
    if n in key:
        print(season_dict[key])
        break
else:
    print('Check the number of months in a year!')
