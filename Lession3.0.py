# Задача 1. Зоопарк
# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# index_bear = zoo.index('lion')
# zoo.insert(index_bear + 1,'bear')
# print(f'Завезли медведя: \n{zoo}')
#
# zoo.remove('elephant')
# print(f'Увезли слона: {zoo}')
# print('Лев сидит в клетке номер:', zoo.index('lion') + 1)
# print('Обезьяна сидит в клетке номер:', zoo.index('monkey') + 1)

# Задача 2. Сокращения
# list_peaople = []
# count_p = int(input('Введите кол-во сотрудников: '))
# for i in range(count_p):
#     money = int(input(f'Зарплата {i+1} сотрудника: '))
#     list_peaople.append(money)
#
# for index in list_peaople:
#     if index == 0:
#         list_peaople.remove(index)
# print('Осталось сотрудников: ', len(list_peaople))
# print(f'Зарплаты: {list_peaople}')
#
# print(f'Максимальная зп: {max(list_peaople)}')
# print(f'Минимальная зп: {min(list_peaople)}')

# Задача 3. Кино
# def movie_films(movie,all_movie):
#     for i in all_movie:
#         if i == movie:
#             return True
#     return False
# films = [
#
#  'Крепкий орешек', 'Назад в будущее', 'Таксист',
#
# 'Леон', 'Богемская рапсодия', 'Город грехов',
#
# 'Мементо', 'Отступники', 'Деревня',
#
#  'Проклятый остров', 'Начало', 'Матрица'
#
# ]
# my_films = []
# print('Добро пожаловать!')
# while True:
#     print(f'Ваш текущий список фильмов: {my_films}')
#     name_film = input('Введите название фильма: ')
#     if movie_films(name_film,films):
#         action = input('Команды: добавить, вставить, удалить')
#         if action == 'добавить':
#             if movie_films(name_film,my_films):
#                 print('Этот фильм есть в вашем списке!')
#             else:
#                 my_films.append(name_film)
#
#         if action == 'вставить':
#             number_action = int(input('На какое место: '))
#             my_films.insert(number_action,name_film)
#         if action == 'удалить':
#             if movie_films(name_film,my_films):
#                 my_films.remove(name_film)
#
#     else:
#         print('Такого фильма в нашем списке!')