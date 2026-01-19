#Задача 1. Заказ фруктов
# order = {
#     'apple': 2,
#     'banana': 3,
#     'pear': 1,
#     'watermelon': 10,
#     'chocolate': 5,
#          }
# print(order.get('orange',0))
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
# sum_price = 0
# count_frutis = 0
# for k_1,v_1 in order.items():
#     print(f'\nФрукт {k_1} в количестве {v_1}')
#     count_frutis += v_1
#     sum_price += incomes.get(k_1,0) * v_1
# print(f'Сумма фруктов: {sum_price}, количество {count_frutis}')

#Задача 2. Игроки
# layers_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
#
# }
# one_list = [player['name']
#             for player in layers_dict.values()
#             if player['team'] == 'A' and player['status'] == 'Rest'
#             ]
# print(f'Все члены команды А, которые отдыхают: {one_list} ')
# ################################################################
# two_list = [player['name']
#             for player in layers_dict.values()
#             if player['team'] == 'B' and player['status'] == 'Training'
#             ]
# print(f'Все члены команды B, которые тренируются: {two_list}')
#
# free_list = [player['name']
#             for player in layers_dict.values()
#             if player['team'] == 'C' and player['status'] == 'Travel'
#             ]
# print(f'Все члены команды C, которые путешествуют: {free_list}')

#