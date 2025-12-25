# Lession 2.1
# numbers = [3, 7, 5]
# while True:
#     number = int(input('Новое число: '))
#     numbers.append(number)
#     print('Текущий список чисел:', numbers)
#     for i in numbers:
#      print(i ** 2, i ** 3, i ** 4)
#
#     print()

#Задача 2. Очень простая задача

# numbers = [i for i in range(100)]
# print(f'Созданный список: {numbers}')

#Задача 3. Контроль
# list_id = []
# count_id = int(input('Введите кол-во людей в офисе: '))
# for _ in range(count_id):
#     new_id = int(input('ID сотрудника: '))
#     list_id.append(new_id)
# print(f'Новый список сотрудников: {list_id}')
# search_id = int(input('Введите ID сотрудника: '))
# if search_id in list_id:
#     print('Сотрудник найден!')
# else:
#     print('Сотрудника нет')


#Задача 1. Гугл
# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
# maximum = 0
# minimum = 0
# for i in nums_list:
#     if maximum < i:
#         maximum = i
#     if minimum <= i:
#         minimum = i
# print('Максимальное число в списке:', max(nums_list))
# print('Минимальное число в списке:', min(nums_list))

#задание 2
# count_list = int(input('Введите кол-во чисел в списке: '))
# list_number = []
# for i in range(count_list):
#     print(f'Введите число {i + 1}:',end=' ')
#     numbers = int(input())
#     list_number.append(numbers)
# print(f'Лист выглядит так: {list_number}')
# divider = int(input('Введите делитель: '))
# for index in range(len(list_number)):
#     if list_number[index] % divider == 0:
#         print(f'Индекс числа {list_number[index]}: {index}')

# Задание 3
# N = [15,25,45,55,65,85]
# new_list = []
# min_num = N.index(min(N))
# max_num = N.index(max(N))
# print(f'Старый список: {N}')
#
# N.index(min(N)), N.index(max(N)) == N.index(max(N)),N.index(min(N))
# N[min_num], N[max_num] = N[max_num],N[min_num]
# print(N)
#

# print(f'Новый список: {new_list}')

# text = input('Введите текст: ')
# count = [0]
# list_text = list(text)
# for index in range(len(list_text)):
#     if list_text[index] == ':':
#         list_text[index] = ';'
#         count[0] += 1
# print(f'Изменнёный текст:',end=' ')
# for i in list_text:
#     print(i,end='')
#
# print(f'\nКол-во изменений: {count[0]}')

# text = input('Введите строку: ')
# list_text = list(text)
# number = int(input('Номер символа: '))
# print(f'Символ слева: {list_text[number-2]}')
# print(f'Символ справа: {list_text[number]}')
# if list_text[number - 1] == list_text[number - 2] or list_text[number - 1] == list_text[number]:
#     print('Есть ровно один такой же символ')
# else:
#     print('Таких же символов нет!')
#
# word_list = []
# count_list = [0,0,0]
# for i in range(3):
#     new_word = input(f'Введите {i + 1} слово: ')
#     word_list.append(new_word)
#
# text = input('Слово из текста: ')
# while text != 'end':
#     text = input('Слово из текста: ')
#     for index in range(3):
#         if text == word_list[index]:
#             count_list[index] += 1
#
# print(f'Подсчёт слов в текст: ')
# for index in range(3):
#     print(f'{word_list[index]}:{count_list[index]}')

# n = int(input('Введите число: '))
# n_list = [i for i in range(n + 1) if i % 2 != 0]
# print(f'Список нечётных чисел от одного до {n}: {n_list}')

# name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
# new_name_list = [name_list[index] for index in range(len(name_list)) if index % 2 == 0]
# print(f'Первый день: {new_name_list}')

# count_video = int(input('Количество видеокарт: '))
# all_videos = []
# for i in range(count_video):
#     models = int(input(f'Видеокарта {i}: '))
#     all_videos.append(models)
# print(f'Старый список видеокарт: {all_videos}')
# new_list = []
# for index in range(len(all_videos)):
#     if all_videos[index] != max(all_videos):
#         new_list.append(all_videos[index])
# print(f'Новый список: {new_list}')

#Zadanie 4
# films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
# new_list_films = []
# count_films = int(input('Сколько фильмов хотите добавить? '))
# for i in range(count_films):
#     name_film = input('Введите название фильма: ')
#     if name_film in films:
#         new_list_films.append(name_film)
#     else:
#         print(f'Ошибка: Фильм {name_film} у нас нет :(')
# print(f'Ваш список любимых фильмов:',end=' ')
# for i in new_list_films:
#     print(i,end=',')

# count_c = int(input('Кол-во контейнеров: '))
# list_c = []
# for _ in range(count_c):
#     weight = int(input('Введите вес контейнера: '))
#     list_c.append(weight)
# new_weight = int(input('Введите вес нового кон-ра: '))
# list_c.append(new_weight)
# list_c.sort(reverse=True)
# final = list_c.index(new_weight)
# print(f'Номер который получит новый контейнер: {final + 1} ')

#Zadanie 7
# text = input('Введите слово: ')
# new_text = list(text)
# new_text_two = new_text[::-1]
# if new_text == new_text_two:
#     print('Слово является палиндромом')
# else:
#     print('Слово не является палиндромом')

#zadanie 8
# old_list = [1, 4, -3, 0, 10]
# print(f'Изначальный список: {old_list}')
# old_list.sort()
# print(f'Отсортированный список: {old_list}')

#Homework 1
# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
# first_company = [0, 0, 0]
# second_company = [1, 0, 0, 1, 1]
# third_company = [1, 1, 1, 0, 1]
# main.extend(first_company)
# main.extend(second_company)
# main.extend(third_company)
# print(f'Общий список компании: {main}')
# print('Количество не выполненных задач: ',main.count(0))

# Задача 2. Вредоносное ПО
# def summary(my_list):
#     lists = [i for i in my_list]
#     all_s = lists.count('?') + lists.count('!')
#     return all_s
#
# second_text = input('Введите первое сообщение: ')
# first_text = input('Введите второе сообщение: ')
# second_list = [i for i in second_text]
# first_list = [i for i in first_text]
# # second_list.extend(sуcond_text)
# # first_list.extend(first_text)
# count_second = summary(second_list)
# count_first = summary(first_list)
# if count_second > count_first:
#     second_list.extend(first_list)
#     for i in second_list:
#         print(i,end='')
# elif count_second < count_first:
#     first_list.extend(second_list)
#     for i in first_list:
#         print(i,end='')
# elif count_second == count_first:
#     print('ОЙ')

# Задача 3. Пакеты
# decode = []
# list_packs = []
# packs = int(input('Кол-во пакетов? '))
# for pack in range(packs):
#     print('\nПакет номер',pack + 1)
#     for i in range(4):
#         print('\n',i + 1,'бит:',end='')
#         bit = int(input(''))
#         decode.append(bit)
#     if decode.count(-1) <= 1:
#         list_packs.extend(decode)
#     else:
#         print('Много ошибок в пакете!')
#         decode = []
# print(f'Полученное сообщение: {list_packs}')
# print('Кол-во ошибок в сообщении: ',list_packs.count(-1))

# Задача 1. Матрица
# matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
# for index in matrix:
#     for i in index:
#         print(i,end=' ')
#     print('')

# Задача 2. Олимпиада
# number_people = int(input('Кол-во участников: '))
# number_teams = int(input('Кол-во команд: '))
# if number_people % number_teams != 0:
#     print(f'{number_people} участников не возможно поделить на команды по {number_teams} человек!')
# else:
#     num = 1
#     all_list = []
#     for peaople in range(number_people // number_teams):
#         all_list.append(list(range(num, num + number_teams)))
#         num += number_teams
#     print(all_list)


# Задача 3. Лавка
# goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
# print(f'Текущий ассортимент: {goods}')
# new_fruit = ['', 0]
# new = input('Новый фрукт: ')
# price = int(input('Цена: '))
# goods.append([new,price])
# print(f'Новый ассортимент: {goods}')
# for frut in goods:
#     frut[1] += frut[1] * 8 / 100
#
# print(f'Новый ассортимент с увел. ценой: {goods}')

# def merge_sorted_lists(l1,l2):
#     all_list = []
#     for i in l1:
#         if i not in l2:
#             all_list.append(i)
#     for i_2 in l2:
#         if i_2 not in l1:
#             all_list.append(i_2)
#     return sorted(all_list)
# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 5, 6, 8, 10]
# merged = merge_sorted_lists(list1, list2)
# print(merged)

#Final_HomeWork!
#1
# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# print('Количество цифр 5 при первом объединении: ',a.count(5))
# a = [i for i in a if i != 5 ]
# print(a)
# for i in c:
#     a.append(i)
# print('Количество цифр 3 при втором объединении: ',a.count(3))
# # a = [i for i in a if i != 3 ]
# print('Итоговый список: ',a)

#2
# def merge_sorted_lists(l1,l2):
#     all_list = sorted(list(set(l1 + l2)))
#     return all_list
# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 5, 6, 8, 10]
    # all_list = []
    # all_list.extend(list1)
    # all_list.extend(list2)
    # for index in all_list:
    #     if all_list.count(index) > 2:
    #         all_list.remove(index)
    # print(sorted(all_list))

# merged = merge_sorted_lists(list1, list2)
# print(merged)

# #3
# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
# name_detail = input('Введите название детали: ')
# final_list = [0,0]
# for i in shop:
#     if i[0] == name_detail:
#         final_list[0] += i[1]
#         final_list[1] += 1
#
# if final_list[1] > 0:
#     print(f'Кол-во деталей: {final_list[1]}')
#     print(f'Общая стоимость деталей: {final_list[0]}')
# else:
#     print('Таких деталей нет в наличии.')

#3
# guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
#
# while True:
#     print(f'\nСейчас на вечеринке {len(guests)} человек: {guests}')
#     question = input('Гость пришёл или ушёл?')
#     if question == 'пришёл':
#         name_guest = input('Имя гостя: ')
#         if len(guests) == 6:
#             print('Прости',name_guest,',но мест нет.')
#         else:
#             guests.append(name_guest)
#
#     if question == 'ушёл':
#         name_guest = input('Имя гостя: ')
#         print('Пока',name_guest,'!')
#         guests.remove(name_guest)
#
#     if question == 'пора спать':
#         print('Вечеринка закончилась, все легли спать.')
#         break

#5
# violator_songs = [
#
# ['World in My Eyes', 4.86],
#
# ['Sweetest Perfection', 4.43],
#
# ['Personal Jesus', 4.56],
#
# ['Halo', 4.9],
#
# ['Waiting for the Night', 6.07],
#
# ['Enjoy the Silence', 4.20],
#
# ['Policy of Truth', 4.76],
#
# ['Blue Dress', 4.29],
#
# ['Clean', 5.83]
#
# ]
# music = 0
# number = int(input('Сколько песен выбрать? '))
# for i in range(number):
#     print(f'Название {i + 1}-й песни: ',end='')
#     name_m = input()
#     for index in violator_songs:
#         if index[0] == name_m:
#             music += index[1]
# print(f'Общее время звучания песен - {round(music,2)}')

#6
# list_rolls = []
# count_rolls = int(input('Количество роликов? '))
# for i in range(count_rolls):
#     print(f'Размер пары {i + 1}',end='')
#     size = int(input())
#     list_rolls.append(size)
# list_peaople = 0
# count_peaople = int(input('Количество людей: '))
# for index in range(count_peaople):
#     print(f'Размер ноги человека {index + 1}:',end='')
#     size_peaople = int(input())
#     if size_peaople in list_rolls:
#         list_peaople += 1
#         list_rolls.remove(size_peaople)
#
# print('Наибольшее количество людей, которые могут взять ролики: ', list_peaople)

#7
# N = int(input('Кол-во людей: '))
# K = int(input('Какое число в считалке: '))
# people = [list(range(1,N + 1))]
# out = 0
# print(f'Выбывает каждый {K}-й человек')
# print(f'Текущий круг людей: {people}')
# for i in range(N-1):
#     print('Текущий круг людей', people)
#     start_count = out % len(people)
#     out = (start_count + K - 1) % len(people)
#     print('Начало счёта с номера', people[start_count])
#     print('Выбывает человек под номером', people[out])
#     people.remove(people[out])
# print()
# print('Остался человек под номером', people[0])
#
# #9
# num_list = []
# number_list = []
# num_count = int(input('Количество чисел: '))
# for _ in range(num_count):
#     print('Число: ',end=' ')
#     n = int(input(''))
#     num_list.append(n)
#
# print(f'Последовательность: {num_list}')
#
# counter = 0
# while num_list != num_list[::-1]:
#     num_list.insert(num_count,num_list[counter])
#     print(num_count)
#     counter += 1
#
# print(f'Нужно приписать чисел: {counter}')
# print(f'Сами числа: {num_list[:counter][::-1]}')
#
# left = int(input('Левая граница: '))
# high = int(input('Правая граница: '))
#
# cubs_list = [x ** 3 for x in range(left,high + 1)]
# k_list = [x ** 2 for x in range(left,high + 1)]
#
# print(f'Список кубов чисел в диапазоне от {left} до {high}: {cubs_list}')
# print(f'Список квадратов чисел в диапазоне от {left} до {high}: {k_list}')

# text = input('Введите строку: ')
# text_second = input('Введите дополнительный символ: ')
#
# first_list = [x * 2 for x in list(text)]
# second_list = [x + text_second for x in first_list]
#
# print(f'Список удвоенных символов: {first_list}')
# print(f'Склейка с дополнительными символами: {second_list}')

# def price_procent(price,procent):
#     new_price = (price * procent) / 100
#     price += new_price
#     return price
#
# one_year = [float(input('Цена на товар: ')) for _ in range(5)]
# first_year = int(input('Повышение на первый год: '))
# second_year = int(input('Повышение на второй год: '))
#
# two_year = [price_procent(x,first_year) for x in one_year]
# free_year = [price_procent(x,second_year) for x in two_year]
#
# print('Сумма цен за каждый год: ',round(sum(one_year), 2), round(sum(two_year), 2), round(sum(free_year), 2) )

# # Задача 1. Список чётных чисел
# num_1 = int(input('Число 1: '))
# num_2 = int(input('Число 2: '))
# n_list = [x ** 2 for x in range(num_1,num_2 + 1) if x % 2 == 0]
# print(f'Итоговый список: {n_list}')

#Задача 2. Магазин
# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# new_list = [(x if x > 0 else 0)for x in original_prices]
# print(f'Результат: {new_list}')

#Задача 3. Отряды
# import random
# team_1 = [random.randint(50,80) for _ in range(10)]
# team_2 = [random.randint(30,60) for _ in range(10)]
# team_3 = [('Погиб' if team_1[i_damage] + team_2[i_damage] > 100
#            else 'Выжил')
#           for i_damage in range(10)]
# print(f'Урон первого отряда: {team_1}')
# print(f'Урон второго отряда: {team_2}')
# print(f'fСостояние третьего отряда: {team_3}')

#
#import random
# original_prices = [random.randint(-5,5) for _ in range(7)]
# original_prices = [-12, 3, 5, -2, 1]
# new_prices = original_prices[:]
#
# for i in range(len(original_prices)):
#     if new_prices[i] < 0:
#         new_prices[i] = 0
# print(f'Первый список: {original_prices}')
# print(f'Второй список: {new_prices}')
#print("Мы потеряли: ", sum(original_prices) - sum(new_prices))

#Задача 2. Срезы
# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
# #В первой строке выведите первые пять элементов списка.
# print(nums[:5])
# #Во второй строке выведите весь список, кроме последних двух элементов.
# print(nums[:-2])
# # В третьей строке выведите все элементы с чётными индексами.
# print(nums[::-1][::2])

#Задача 3. Удаление части
# import random
# numbs = [random.randint(1,10) for _ in range(10)]
# print(f'Первый список: {numbs}')
# a = random.randint(0,4)
# b = random.randint(4,8)
# print('Новый список: ',numbs[0:a] + numbs[b:])

#///////////////////////////////////////////////////////////////

#Задание 1. Гласные буквы
# text = list(input('Введите текст: '))
# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# new_list = [i for i in text if i in vowels]
# print(f'Список гласных букв: {new_list}')
# print(f'Длина списка: {len(new_list)}')

#Задание 2. Генерация
# numb = int(input('Введите число: '))
# list_numbs = [1 if i % 2 == 0 or i == 0 else i % 5 for i in range(numb)]
# print(f'Итоговый список: {list_numbs}')

#3 Задание 3. Случайные соревнования
# import random
# team_1 = [round(random.uniform(5.0, 10.0),2) for _ in range(10)]
# team_2 = [round(random.uniform(5.0, 10.0),2) for _ in range(10)]
# print(f'Первая команда: {team_1}')
# print(f'Вторая команда: {team_2}')
# final_list = [round(team_1[i],2) if team_1[i] > team_2[i] else round(team_2[i],2) for i in range(10)]
# print(f'Результаты: {final_list}')

#Задание 4. Тренировка со срезами
# alphabet = 'abcdefg'
# print('1',alphabet[::])
# print('2',alphabet[::-1])
# print('3',alphabet[::2])
# print('4',alphabet[1::2])
# print('5',alphabet[:1])
# print('6',alphabet[-1:])
# print('7',alphabet[3:4])
# print('8',alphabet[-3::])
# print('9',alphabet[3:5])
# print('10',alphabet[3:5][::-1])

#Задание 5. Разворот
# text = input('Введите строку: ')
# n1 = text.index('h')
# n2 = text.rindex('h')
# print('Развёрнутая последовательность между первым и последним h:',text[n1 + 1:n2][::-1])

# #Задание 6. Двумерный список
#
# numb_list = [[j + i for i in range(0,9,4)] for j in range(1,5)]
# print(numb_list)

#Задание 7. Список списков
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# new_list = [k for i in (range(len(nice_list)))
#             for j in range(len(nice_list[i]))
#             for k in nice_list[i][j]]
# print(new_list)

#Задание 8. Шифр Цезаря
# RUSSIAN_LOWERCASE = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# list_rus = list(RUSSIAN_LOWERCASE)
# text = input('Введите сообщение: ')
# step = int(input('Введите сдвиг: '))
# index = 0
# encrypted = [list_rus[(list_rus.index(i) + step) % len(list_rus)]
#              if i in list_rus else i for i in text.lower()]
# print('\nСообщение: ')
# for j in encrypted:
#     print(j,end='')