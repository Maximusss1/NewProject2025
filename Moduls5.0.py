# Задача 1. Заказ
# name = input('Имя: ')
# number = int(input('Номер заказа: '))
# text = 'Здравствуйте, {name_profile}!, Ваш номер заказа: {num} . Приятного дня!'.format(
#     name_profile=name,
#     num=number)
# print(text)

# Задача 2. Долги
# name = input('Введите имя: ')
# gold = int(input('Введите долг: '))
# text = '{name_friend}! {name_friend},привет! Как дела, {name_friend}? Где мои {money} рублей? {name_friend}!'.format(
#     name_friend=name,
#     money=gold)
# print(text)

#Задача 3. IP-адрес
# ip_adress = list(input('Введите число в диапозоне от 0 до 255').split('.'))
# if len(ip_adress) < 4:
#     print('Должен состоять из 4 чисел, от 0 до 255!')
# else:
#     num = 0
#     out = 0
#     for i in ip_adress:
#         if i.isdigit():
#             num+=1
#             if int(i) > 255:
#                 out += 1
#                 print('Ошибка! Число должно быть в диапозоне 0 - 255!')
#         else:
#            out += 1
#            print(f'{i} - это не целое число!')
#     if num == 4 and out == 0:
#         print(f'Ip - адресс корректный!')
#     else:
#         print(f'{ip_adress} не корректный адресс!')

################# 5.3 Методы строк: split и join
# Задача 1. Улучшенная лингвистика 2
# word = input('Введте три слова через пробел: ').split()
# text = input('Введите текст: ').split()
# print(f'Список слов: {word}')
# print(f'Список текста: {text}')
# counts = 0
# for i in range(len(word)):
#     counts += text.count(word[i])
# print(f'Слова встретилисть {counts} раз.')

#Задача 2. Бабушка
# text = input('Введите текст: ').split()
# # new_text = " ".join(text)
# print(f'Исправленный текст: {text}')

#Задача 3. Разделители символов
# text_happy = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}:\n')
# if '{name}' in text_happy and '{age}' in text_happy:
#     name_list = input('Список людей через запятую: ').split(',')
#     age_list = input('Возраст людей через пробел: ').split()
#     for i in range(len(name_list)):
#         print(text_happy.format(name=name_list[i],age=age_list[i]))
#     final_list = [' '.join([name_list[i], str(age_list[i])])
#         for i in range(len(name_list))]
#     final_str = ','.join(final_list)
#     print(f'Именниники: {str(final_str)}')
# else:
#     print('В тексте отствует одна или две конструкции!')

#5.4 Методы строк: startswith, endswith, upper, lower 5.4 Методы строк: startswith, endswith, upper, lower

#Задача 1. Шифр Цезаря 2
# alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.lower()
# text = input('Введите текст: ')
# number = int(input('Введите сдвиг: '))
# new_text = [alf[(alf.index(i) + number) % len(alf)] if i != ' ' else ' ' for i in text.lower()]
# new_text = ''.join(new_text)
# print(f'Получился штифр: {new_text}')

#Задача 2. Путь к файлу
# disk = input('Введите диск: ')
# rash = input('Введите расширение: ')
# path = '{dis}:/user/docs/folder/new_file{ra}'.format(dis=disk,ra=rash)
# if not path.startswith('C:/'):
#     print('Диск должен быть C !')
# elif not path.endswith('.txt'):
#     print('Не правильное расширении файла!')
# else:
#     print('Путь корректен!')

#Задача 3. Удаление части
# text = input('Введите строку: ')
# t_upper = sum([1 for i in text if i.isupper()])
# t_lover = sum([1 for i in text if i.islower()])
# if t_lover > t_upper:
#     print(f'Результат: {text.lower()}')
# elif t_lover < t_upper:
#     print(f'Результат: {text.upper()}')
# else:
#     print(f'Результат: {text}')

