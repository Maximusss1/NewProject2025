# 7.9 Практическая работа
# Задача 1. Ревью кода
# def is_interes_and_surname(object:dict):
#     all_interes = [volue for key in object
#                    for volue in object[key]['interests']]
#     count_surname = 0
#     for key in students:
#         for v in object[key]['surname']:
#             count_surname += 1
#     return (all_interes,count_surname)
#
# students = {
#     1: {
#         'name': 'Bob',
#         'surname': 'Vazovski',
#         'age': 23,
#         'interests': ['biology, swimming']
#     },
#     2: {
#         'name': 'Rob',
#         'surname': 'Stepanov',
#         'age': 24,
#         'interests': ['math', 'computer games', 'running']
#     },
#     3: {
#         'name': 'Alexander',
#         'surname': 'Krug',
#         'age': 22,
#         'interests': ['languages', 'health food']
#     }
# }
# list_id_age = [(key,students[key]['age']) for key in students]
# print(f'Список пар «ID студента — возраст»: {list_id_age}')
# result_1,result_2 = is_interes_and_surname(students)
# print(f'Полный список интересов всех студентов: {result_1}')
# print(f'Общая длина всех фамилий студентов: {result_2}')

#2Задача 2. Универсальная программа
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2,int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def crypto(object):
#     final_list = []
#     for k,v in enumerate(object):
#         if is_prime(k):
#             final_list.append(v)
#     return final_list
#
# print(f'Ответ в консоли: ',end='')
# # print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(crypto('О Дивный Новый мир!'))

#Задача 3. Игроки
# players = {
#     ("Ivan", "Volkin"): (10, 5, 13),
#     ("Bob", "Robbin"): (7, 5, 14),
#     ("Rob", "Bobbin"): (12, 8, 2)
# }
# result = [(k + v) for k,v in players.items()]
# print(result)

# Задача 4. По парам
# one_list = [n for n in range(10)]
# print(f'Первый список: {one_list}')
# two_list = for i in one_list]
# print(two_list)

#Задача 5. Функция сортировки
# def tpl_sort(object:tuple):
#     for n in object:
#         if type(n) == float:
#             return object
#     return sorted(object)
#
# tpl = (6, 3, -1, 8, 4, 10, -5)
# print(tpl_sort(tpl))

#Задача 6. Контакты — 3
# books = {}
# while True:
#     print(f'\nВаши контакты: {books}')
#     what = int(input('Введите номер действия:\n1-Добавить контакт.2-Найти человека.'))
#     if what == 1:
#         name_person = tuple(input(f'Введите имя и фамилию нового контакта (через пробел):').split())
#         if name_person not in books.keys():
#             telephone = int(input('Введите номер телефона: '))
#             books[name_person] = telephone
#         else:
#             print(f'Такой контакт уже существует в списке!')
#     elif what == 2:
#         search = input('Введите фамилию для поиска:')
#         for k,v in books.items():
#             if k[1] == search:
#                 print(k[0],k[1],'-',v)

#Задача 7. Своя функция zip
# def list_gen(object_,lenght):
#     gen_list = []
#     count = 0
#     for i in object_:
#         gen_list.append(i)
#         count += 1
#         if count == lenght:
#             return gen_list
#
# def my_zip(object_1,object_2):
#     zipped = []
#     min_len = min(len(object_1), len(object_2))
#     for i in range(min_len):
#         zipped.append((list_gen(object_1,min_len)[i], list_gen(object_2,min_len)[i]))
#     return zipped
#
#
# strin = 'abcd'
# tupl = (10, 20, 30, 40)
# new_list = zip(strin,tupl)
# print(new_list)
# for item in new_list:
#     print(item)
#
# print()
#
# new_list = my_zip(strin,tupl)
# print(new_list)
# for item in new_list:
#     print(item)
