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