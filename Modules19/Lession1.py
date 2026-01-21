#Задача 1. Словарь квадратов чисел
# num = 5
# dict_n = {}
# for i in range(1,6):
#     dict_n[i] = i ** 2
# print(dict_n,'\n')

#Задача 2. Студент
# p = 'имя,фамилия,город,место учёбы,оценки'.split(',')
# text = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки):').split()
# dict_one = {}
# dict_one['имя'] = text[0]
# dict_one['фамилия'] = text[1]
# dict_one['город'] = text[2]
# dict_one['место учёбы'] = text[3]
# dict_one['оценки'] = text[4:]
# for k,v in dict_one.items():
#     print(k,'-',v)

#Задача 3. Контакты
# dict_contacts = {}
# while True:
#     print(f'\nТекущие контакты на телефоне: ')
#     if len(dict_contacts) > 0:
#         #new = dict_contacts.keys()
#         for k,v in dict_contacts.items():
#             print(k,v)
#     else:
#         print('<Пусто>')
#     name = input('Введите имя: ')
#     if name not in dict_contacts:
#         number = input('Введите номер телефона')
#         dict_contacts[name] = number
#     else:
#         print(f'Имя {name} уже есть в телефоной книге.')





