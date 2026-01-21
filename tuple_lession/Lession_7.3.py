# Задача 1. Саботаж!
# input_word = input('Введите строку: ')
# print(f'Ответ: ',end=' ')
# for index, text in enumerate(input_word):
#     if text == '~':
#         print(index,end=' ')

# # Задача 2. Словари из списков
# import string
# import random
# one_list = [random.choice(string.ascii_uppercase) for _ in range(10)]
# two_list = [random.choice(string.ascii_uppercase) for _ in range(10)]
# print(f'Первый список: {one_list}')
# print(f'Второй список: {two_list}')
# one_dict = {}
# two_dict = {}
# for k,v in enumerate(one_list):
#     one_dict[k] = v
# for k,v in enumerate(two_list):
#     two_dict[k] = v
# print(f'Первый словарь: {one_dict}')
# print(f'Второй словарь: {two_dict}')

# #Задача 3. Универсальная программа
# def result(text):
#     if isinstance(text,dict):
#         return [text[value] for key,value in enumerate(text) if key % 2 == 0]
#     else:
#         return [value for key, value in enumerate(text) if key % 2 == 0]
#
#
# user_data = [100, 200, 300, 'буква', 0, 2, 'а']
# ser_data = 'О Дивный Новый мир!'
# print(result(user_data))
# print(result(ser_data))