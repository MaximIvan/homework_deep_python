"""
1. Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит 
уникальные (без повтора) элементы исходного списка. 
*Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
"""

# nums = [1, 2, 1, 3, 2]
# print(set(nums))

# for num in nums:
#     while nums.count(num) > 1:
#         nums.remove(num)
# print(nums)

# res = []

# for num in nums:
#     if num not in res:
#         res.append(num)
# print(res)


"""
2. Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
"""

# atributes = ['qwqw', '1221', '12.01', 'anFanf', 'fafnajfn1112122', '-12', '0']

# for attr in atributes:
#     if attr.lstrip('-').isdigit():
#         res = abs(int(attr))
#         print(res,type(res))
#     elif attr.count('.') == 1:
#         if attr.replace('.', '', 1).isdigit():
#             res = float(attr)
#             print(res, type(res))
#     elif attr != attr.lower():
#         print(attr.lower())
#     else:
#         print(attr.upper())

"""
3. ✔ Создайте вручную кортеж содержащий элементы разных типов. 
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""

# attributes = ('str', 1, 3, 111, -200, 
#               '12313', 'gggg', True, False,
#               12.111, 14.11, 3.14, [1, 33, 'str'])

# res = {}

# for attr in attributes:
#     res.setdefault(type(attr), []).append(attr)

# print(res)


"""
4. ✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""

# nums = [1, 2, 1, 3, 2, 1, 1]

# for num in nums:
#     counter = nums.count(num)
#     if counter > 1 and counter % 2 == 0:
#         for _ in range(counter):
#             nums.remove(num)
    
#     while nums.count(num) % 2 == 0 and num in nums:
#         nums.remove(num)
#         nums.remove(num)
# print(nums)


"""
5. ✔ Создайте вручную список с повторяющимися целыми числами. 
✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка. 
✔ Нумерация начинается с единицы.
"""

# my_list = [1, 2, 3, 2, 1, 5, 7, 3, 2]
# new_list = []

# for i, elem in enumerate(my_list, start=1):
#     if elem % 2 != 0:
#         new_list.append(i)

# print(new_list)

"""
6. Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
"""

# my_str = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки.'
# my_list = sorted(my_str.split())

# max_len = len(max(my_list, key=len))

# for i, elem in enumerate(my_list, start=1):
#     print(f'{i} {elem:>{max_len}}')

"""
7. ✔ Пользователь вводит строку текста. 
✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним. 
✔ Результат сохраните в словаре, где ключ —символ, а значение — частота встречи символа в строке. 
✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.
"""

# my_str = 'Пользователь вводит строку текста'
# my_str = my_str.replace(' ', '')

# my_dict = {}

# for i in my_str:
#     my_dict[i] = my_str.count(i)
# print(my_dict)

# for i in my_str:
#         my_dict[i] += my_dict.get(i, 0) + 1
# print(my_dict)


"""
8. ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

# item_dict = {'Вася': {'рюкзак', 'палатка', 'котелок', 'фонарик'},
#              'Коля': {'рюкзак', 'палатка', 'фонарик', 'спички'},
#              'Миша': {'рюкзак', 'палатка', 'спички', 'велосипед'}}

# res1 = (item_dict['Вася']) & (item_dict['Коля']) & (item_dict['Миша'])
# print(res1)

# доделать в домашней работе!
