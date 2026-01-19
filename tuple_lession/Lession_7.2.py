# Задача 1. Создание кортежей
# import random
# one_tuple = [random.randint(0,5) for _ in range(10)]
# two_tuple = [random.randint(-5,0) for _ in range(10)]
# free_tuple = tuple(one_tuple + two_tuple)
# print(f'Первый кортеж: {tuple(one_tuple)}')
# print(f'Второй кортеж: {tuple(two_tuple)}')
# print(f'Третий кортеж: {free_tuple}')
# print(f'Кол-во нулей в списке: {free_tuple.count(0)}')

# Задача 2. Цилиндр
# import math
# def side_and_full(r:int,h:int):
#     side = 2 * math.pi * int(r) * int(h)
#     s = math.pi * math.pow(r,2)
#     full = side + 2 * s
#     return side, full
#
# r = float(input('Введите радиус и высоту через пробел: '))
# h = float(input('Введите радиус и высоту через пробел: '))
# side,full = side_and_full(r,h)
# print(f'Прощадь боковой поерхности: {side}')
# print(f'Полная площадь: {full}')

#Задание 3.
# import random
# def change(nums):
#
#     index = random.randint(0, 5)
#     value = random.randint(100, 1000)
#     nums[index] = value
#     return nums, value
#
# my_nums = [1, 2, 3, 4, 5]
#
#
# new_nums, rand_val = change(my_nums)
# print(new_nums, rand_val)
# new_nums, rand_val = change(new_nums)
# rand_val += change(new_nums)[1]
# print(new_nums, rand_val)

