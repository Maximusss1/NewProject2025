# Задание 1. Песни — 2
# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# }
# count_music = int(input('Сколько песен выбрать? '))
# all_music = 0
# for i in range(count_music):
#     name_music = input(f'Название {i+1} песни: ')
#     if name_music in violator_songs:
#         all_music += violator_songs.get(name_music)
#     else:
#         print('Такой песни нет!')
# print(f'Общее время звучания песен: {round(all_music,2)} минут.')

#Задание 2. Криптовалюта
# data = {
#     "address": "0x544444444444",
#     "ETH": {
#     "balance": 444,
#     "totalIn": 444,
#     "totalOut": 4
#         },
#     "count_txs": 2,
#     "tokens": [ {
#     "fst_token_info": {
#     "address": "0x44444",
#     "name": "fdf",
#     "decimals": 0,
#     "symbol": "dsfdsf",
#     "total_supply": "3228562189",
#     "owner": "0x44444",
#     "last_updated": 1519022607901,
#     "issuances_count": 0,
#     "holders_count": 137528,
#     "price": False
#     },
#     "balance": 5000,
#     "totalIn": 0,
#     "total_out": 0
#     },
#     {
#     "sec_token_info": {
#     "address": "0x44444",
#     "name": "ggg",
#     "decimals": "2",
#     "symbol": "fff",
#     "total_supply": "250000000000",
#     "owner": "0x44444",
#     "last_updated": 1520452201,
#     "issuances_count": 0,
#     "holders_count": 20707,
#     "price": False
#     },
#     "balance": 500,
#     "totalIn": 0,
#     "total_out": 0
#     }
#     ]
#     }
# print('Вывести списки ключей и значений словаря. ')
# print(list(data.keys()))
# print(list(data.values()))
#
# print('Внутри fst_token_info значение ключа name поменять с fdf на doge. ')
# data['tokens'][0]['fst_token_info']['name'] = 'dodge'
# print(data['tokens'][0]['fst_token_info']['name'])

# print(data['tokens'][1].update({'price' : 'total price'}))
# new_key = data['tokens'][1].pop('price')
# data['tokens'][1]['Total_price'] = new_key
# new_value = data['tokens'][1]['sec_token_info'].get('price')
# data['tokens'][1]['sec_token_info']['Total_price'] = new_value
# del data['tokens'][1]['sec_token_info']['price']
# print(data['tokens'][1]['sec_token_info'])

#3.Товары.
# goods = {
# 'Лампа': '12345',
# 'Стол': '23456',
# 'Диван': '34567',
# 'Стул': '45678',
# }
# store = {
# '12345': [
# {'quantity': 27, 'price': 42},
# ],
# '23456': [
# {'quantity': 22, 'price': 510},
# {'quantity': 32, 'price': 520},
# ],
# '34567': [
# {'quantity': 2, 'price': 1200},
# {'quantity': 1, 'price': 1150},
# ],
# '45678': [
# {'quantity': 50, 'price': 100},
# {'quantity': 12, 'price': 95},
# {'quantity': 43, 'price': 97},
# ],
# }
#
# for item in goods.keys():
#     # print(item)
#     total_count = 0
#     total_price = 0
#     print('\n')
#     for key in range(len(store[goods[item]])):
#         total_count += store[goods[item]][key]['quantity']
#         total_price += store[goods[item]][key]['quantity'] * store[goods[item]][key]['price']
#     print(f'{item} - {total_count} штук, стоимость {total_price} рублей.')

#Задание 4. Гистограмма частоты — 2
# def func(text):
#     text_dict = {}
#     for item in text:
#         if item not in text_dict:
#             text_dict[item] = 1
#         elif item in text_dict:
#             text_dict[item] += 1
#     return text_dict
#
# input_text = list(input('Введите текст:'))
# one_dict = func(input_text)
# print(f'Оригинальный словарь частот: ')
# for k,v in sorted(one_dict.items()):
#     print(k,':',v)
#
# def func_two(dict_text):
#     two_dict = {}
#     for value in dict_text.values():
#         two_dict[value] = []
#         for key in dict_text.keys():
#             if dict_text[key] == value:
#                 two_dict[value].append(key)
#     return two_dict
#
# two_dict_text = func_two(one_dict)
# print(f'Инвертированный словарь частот: ')
# for k,v in two_dict_text.items():
#     print(f"{k}:{v}")


# #Задание 5. Словарь синонимов
# count_word = int(input('Введите кол-во пар слов: '))
# dict_words = {}
#
# for num in range(count_word):
#     word = input(f'{num + 1}-я пара: ').lower().split()
#     dict_words[word[0]] = word[2]
#
# flag = True
# while flag:
#     input_word = input('Введите слово: ').lower()
#     if input_word not in dict_words.values() and dict_words.keys():
#         print('Нет слова!')
#     else:
#         for k,v in dict_words.items():
#             if input_word == k:
#                 print(v)
#                 flag = False
#             elif input_word == v:
#                 print(k)
#                 flag = False



#7Задание 6. Пицца
# count_orders = int(input('Введите кол-во заказов: '))
# orders = {}
# for num in range(count_orders):
#     bayer, pizza, count = input(f'{num} заказ: ').split()
#     if bayer in orders:
#         if pizza in orders[bayer]:
#             orders[bayer][pizza] = int(count) + int(orders[bayer][pizza])
#         else:
#             orders[bayer].update({pizza:count})
#     else:
#         orders[bayer] = {pizza:count}
#
# for key in orders.keys():
#     print(f'Заказчик: {key}')
#     for k,v in orders[key].items():
#         print(f'{k}:{v}')


#Задание 7. Три списка.
# array_1 = [1, 5, 10, 20, 40, 80, 100]
#
# array_2 = [6, 7, 20, 80, 100]
#
# array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
#
# array_1 = [1, 2, 3, 4]
#
# array_2 = [2, 4]
#
# array_3 = [2, 3]
#
# print('Задание 1:')
# new_list = [i for i in array_1 if i in array_2 and i in array_3]
# print(f'Решение без множеств: {new_list}')
# new_set = set(array_1).intersection(array_2,array_3)
# print(f'Решение с множествами: {new_set}')
#
# print(f'Задание 2: ')
# new_list_2 = [i for i in array_1 if i not in array_2 and i not in array_3]
# print(f'Решение без множеств: {new_list_2}')
# new_set_2 = set(array_1) - (set(array_2) | set(array_3))
# print(new_set_2)

#Задание 8. Снова палиндром
# def text_to_dict(text):
#     sym_dict = dict()
#     for sym in text:
#         if sym in sym_dict:
#             sym_dict[sym] += 1
#         else:
#             sym_dict[sym] = 1
#     return sym_dict
#
# def odd_detector(dict_to_scan:dict):
#     odd_count = 0
#     for sym in dict_to_scan.values():
#         if sym % 2 != 0:
#             odd_count += 1
#         if odd_count > 1:
#             return False
#     return True
#
# def final_func(text):
#     letter_dict = text_to_dict(text)
#     if odd_detector(letter_dict):
#         print('Можно сделать палидромом!')
#     else:
#         print('Нельзя сделать палидромом!')
#
# my_text = input('Введите строку: ')
# final_func(my_text)
