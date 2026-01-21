# #Задание 1. Склады.
# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
#
#
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
# big_storage.update(small_storage)
# search = input('Введите название товара: ')
# if big_storage.get(search) != None:
#     print(f'Товар {search} имеется в количестве: {big_storage[search]} шт.')
# else:
#     print(f'Такого товара нет на складе.')

#Задание 2.Кризис фруктов.
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
# min_frutis = ''
# print('Результат работы программы: ')
# print(f'Общий доход за год составил: {sum(incomes.values())} рублей.')
#
# for k,v in incomes.items():
#     if v == min(incomes.values()):
#         print(f'Самый маленький доход у {k}.Он составляет {v} рублей.')
#         min_frutis = k
# del incomes[min_frutis]
# print(f'Итоговый словарь: {incomes}')

#Задача 3. Гистограмма частоты
# def name_func(string):
#     dict_text = {}
#     for i_sum in string:
#         if i_sum not in dict_text:
#             dict_text[i_sum] = 1
#         else:
#             dict_text[i_sum] += 1
#     return dict_text
#
# text = input('Введите текст: ')
# for k,v in sorted(name_func(text).items()):
#     print(k,':',v)