# site = {
#     'html': {
#         'head': { 'title': 'Мой сайт' },
#
#     'body': {
#         'h2': 'Здесь будет мой заголовок',
#         'div': 'Тут, наверное, какой-то блок',
#         'p': 'А вот здесь новый абзац'
#             }
#             } }
#
# def find_key(object:dict, key:str):
#     if key in object:
#         return object[key]
#
#     for subkey in object.values():
#         if isinstance(subkey, dict):
#             result = find_key(subkey, key)
#             if result:
#                 break
#     else:
#         result = None
#     return result
#
#
# user_key = input('Введите название ключа: ')
# value = find_key(site,user_key)
# if value:
#     print(value)
# else:
#     print('Такой ключ отсутствует в структуре.')