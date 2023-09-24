"""
1.
✔ Напишите функцию, которая принимает строку текста. 
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого 
длинного слова был один пробел между ним и номером строки.
"""

# def sort_by_unicod(text: str):
#     lst_sorted = sorted(text.split())
#     max_word = len(max(lst_sorted, key=len))
#     for i, element in enumerate(lst_sorted, start=1):
#         print(f'{i} {element:>{max_word}}')

# text = 'У нас все хорошо! А будет еще лучше!'
# sort_by_unicod(text)


"""
2.
✔ Напишите функцию, которая принимает строку текста. 
✔ Сформируйте список с уникальными кодами Unicode каждого 
символа введённой строки отсортированный по убыванию.
"""

# def list_sim(str_input):
#     return [ord(i) for i in sorted(list(str_input.replace(' ', '')), reverse=True)]

# # второй вариант через map:

# def list_sim2(str_input):
#     return map(ord,
#                sorted(list(str_input.replace(' ', '')),
#                       reverse=True))


# str_data = 'Напишите функцию, которая принимает строку текста'
# # или:
# # list2 = []
# # for i in sorted(list(str_data.replace(' ', '')), reverse=True):
# #     list2.append(ord(i))

# print(list_sim(str_data))
# print(*list_sim2(str_data))


"""
3. ✔ Функция получает на вход строку из двух чисел через пробел. 
✔ Сформируйте словарь, где ключом будет 
символ из Unicode, а значением — целое число. 
✔ Диапазон пар ключ-значение от наименьшего из введённых 
пользователем чисел до наибольшего включительно.
"""

# def str_to_dict(string: str) -> dict[str, int]:
#     result = {}
#     start, end = sorted(map(int, string.split()))
#     for i in range(start, end + 1):
#         result[chr(i)] = i
#     return result

# print(str_to_dict('2 10'))


"""
4. ✔ Функция получает на вход список чисел. 
✔ Отсортируйте его элементы in place без использования 
встроенных в язык сортировок. 
✔ Как вариант напишите сортировку пузырьком. 
Её описание есть в википедии.
"""

# from typing import List


# def sort_number(numbers: List[int]) -> None:
#     for i in range(len(numbers)):
#         for j in range(i, len(numbers)):
#             if numbers[i] > numbers[j]:
#                 numbers[i], numbers[j] = numbers[j], numbers[i]

# number: List[int] = [7, 954, 91, 37, 7, 1, -4, 6]

# print(number)

# sort_number(number)

# print(number)


'''
Задание №5
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
'''

# names = ['Alex', 'Adam', "eva"]
# salaries = [15000, 20000, 25000]
# awards = ['10.0%', '7.25%', '5%' ]

# def calc_bonus(name: list[str], salary: list[int], award: list[str]) -> dict[str, float]:
#     result = {}
#     for name, salary, award in zip(names, salaries, awards):
#         bonus_amount = salary * float(award[:-1]) / 100
#         result[name] = bonus_amount
#     return result
#     #return {name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)} #выше код записывается одной строкой

# print(calc_bonus(names, salaries, awards))


''' Задание №6
 ✔ Функция получает на вход список чисел и два индекса.
 ✔ Вернуть сумму чисел между переданными индексами.
 ✔ Если индекс выходит за пределы списка, сумма считается
 до конца и/или начала списка.
 '''

# num_list = [1, 5, 7, -9, 0]

# def sunnator(num_list: list[int], index_1: int, index_2: int) :
#     if index_1 > index_2:
#         return 0

#     return sum(num_list[max(index_1, 0):min(index_2+1, len(num_list))])

# print(sunnator(num_list, -3, 10))


'''Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
'''


# dict1 = {"company_1":[1, 2, 5, -8, 10, 36],
#         "company_2":[-10, 2, -19, 7, -15, 36],
#         "company_3":[10, 2, 19, -7, 11, 36]}

# def income(input_dict: dict[str, list[int]]) -> bool:
#     dict2 = {}
#     for value, key in enumerate(input_dict):
#         dict2[key] = sum(input_dict[key])

#     print(dict2)
#     if all(map(lambda x: x > 0, dict2.values())):
#         return True
#     else:
#         return False

# print(income(dict1))

# # короткий вариант решения
# def income1 (input_dict: dict[str, list[int]]) -> bool:
#         for key in input_dict:
#             if sum(input_dict[key]) <= 0:
#                 return False

#         return True

# print(income1(dict1))


"""
8. ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
✔ Напишите функцию, которая при запуске заменяет содержимое переменных 
оканчивающихся на s (кроме переменной из одной буквы s) на None. 
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

# tests = 'test value'
# variables = 'another test value'
# s = 'single letter variable'
# check = 'this variable does not end with s'


# # Redefining the function
# def replace_s_variables():
#     variables_dict = globals()
#     for var_name in list(variables_dict.keys()):
#         if var_name.endswith('s') and var_name != 's':
#             new_var_name = var_name[:-1]
#             variables_dict[new_var_name] = variables_dict[var_name]
#             variables_dict[var_name] = None

# # Let`s first print the initial values of variables
# print('Initial values:')
# print(f'tests: {tests}')
# print(f'variables: {variables}')
# print(f's: {s}')
# print(f'check: {check}')

# # Calling the function
# replace_s_variables()

# # Printing the values of variables after the function execution
# print('\nValues after function execution:')
# print(f'tests: {tests}')
# print(f'variables: {variables}')
# print(f's: {s}')
# print(f'check: {check}')

# # Printing the values of new variables
# print('\nValues of new variables:')
# print(f'test: {test}')
# print(f'variable: {variable}')

# print(f'ГЛОБАЛОЧКИ: {globals()}')