#1
# def person_in(text):
#         if text in data:
#             print(data.get(text))
#         else:
#             print('Таких данных нет!')
#
# data = {
#     (5000, 123456): ('Иванов', 'Василий'),
#     (6000, 111111): ('Иванов', 'Петр'),
#     (7000, 222222): ('Медведев', 'Алексей'),
#     (8000, 333333): ('Алексеев', 'Георгий'),
#     (9000, 444444): ('Георгиева', 'Мария')
# }
# list_dann = tuple([5000,123456])
# print(person_in(list_dann))

#2
# books = {}
# while True:
#     print(f'\nВаша телефона книга: {books}')
#     text = int(input('1-Добавить контакт, 2-Закончить.'))
#     if text == 2:
#         print('До свидания!')
#         break
#     elif text == 1:
#         word = tuple(input('Введите фамилию и имя абонента:').split())
#         if word not in books:
#             number = int(input('Введите номер телефона: '))
#             books[word] = number
#         else:
#             print('Такие Фамилия и Имя уже есть в списке.')
#     else:
#         print('Некорректный ввод! Доступно 1 или 2.')