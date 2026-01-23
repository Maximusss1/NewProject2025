#Задача 1. Работа с файлом
# def fails_programm(qustion,error="Неверный ввод. Пожалуйста, введите 'да' или 'нет'",count=4):
#     while count != 0:
#         word = input(qustion).lower()
#         if word == 'да':
#             return 1
#         elif word == 'нет':
#             return 2
#         else:
#             print(error)
#             count -= 1
#             print(f'Осталось попыток: {count}')
#
# fails_programm('Вы действительно хотите выйти?')
# fails_programm('Удалить файл?',error='Так удалить или нет?')
# fails_programm('Записать файл?',count=2)

#Задача 2. Накопление значений
# def add_num(num,lis_t=[]):
#
#     lis_t.append(num)
#     return lis_t
#
# print(add_num(5))
# print(add_num(10))
# print(add_num(15))

#Задача 3. Помощь другу
# def create_dict(data, template=dict()):
#     if isinstance(data, dict):
#         return data
#     if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
#         return {data:data}
#
#
# def data_preparation(old_list):
#     new_list = []
#     for i_element in old_list:
#         new_list.append(create_dict(i_element))
#     return new_list
#
#
# data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
# data = data_preparation(data)
# print(data)
