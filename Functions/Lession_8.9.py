#Задача 1. Challenge-2
# def suming(start, num):
#
#     if num == start:
#         print(start)
#         return None
#     print(start)
#     return suming(start + 1, num)
#
# print(suming(1,10))

#Задача 2. Поиск элемента — 2.
# site = {
#     'html': {
#         'head': { 'title': 'Мой сайт' },
#     'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац' }
#             }
#         }
# def find_key(key_user,object:dict,max_depyh,cur_depyh=0):
#
#     if key_user in object:
#         return object[key_user]
#
#     cur_depyh += 1
#     if cur_depyh == max_depyh:
#         return None
#
#     for sub_structure in object.values():
#         if isinstance(sub_structure,dict):
#             reusl = find_key(sub_structure,user_key,max_depyh,cur_depyh)
#             if reusl:
#                 break
#     else:
#         reusl = None
#     return reusl
#
#
# user_key = input('Введите название ключа: ')
# my_depyh = int(input('Глубина'))
# key_value = find_key(user_key,site,my_depyh)
# print(key_value)

#Задача 4. Продвинутая функция sum
