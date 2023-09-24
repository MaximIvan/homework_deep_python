'''
1. Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
'''

# def game(num2guess: int, tryes: int):
#     def guessing_game():
#         for _ in range(tryes):
#             if num2guess == int(input('введите число: ')):
#                 return True
#         return False
#     return guessing_game


# if __name__ == '__main__':
#     process = game(10, 3)
#     print(process())


'''
2. Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
'''


# from random import randint

# def game(num2gess: int, tries: int):

#     def guessing_game():
#         for _ in range(tries):
#             if num2gess == int(input('Введите число: ')):
#                 return True
#         return False
#     return guessing_game

# def gaming(func):
#     def wrapper(num2gess: int, tries: int):
#         if not 100 >= num2gess >= 1:
#             num2gess = randint(100, 1)
#         if not 10 >= tries >= 1:
#             tries = randint(10, 1)
#         return func(num2gess, tries)
#     return wrapper

# @gaming
# def guees_num(num2guess: int, tries: int):
#     print(num2guess, tries)
#     for _ in range(tries):
#         if num2guess == int(input("Введите число: ")):
#             return True
#     return False


# if __name__ == "__main__":
#     print(guees_num(101, 11))


'''
3. Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
'''

# import json


# def our_cash(func: callable):
#     try:
#         with open(f'{func.__name__}.json', 'r') as f:
#             data = json.load(f)
#     except FileNotFoundError:
#         data = {}

#     def wrapper(*args, **kwargs):
#         arg = str(args) + str(kwargs)
#         data_res = data.get(arg)
#         if data_res:
#             return data_res
#         result = func(*args, **kwargs)
#         data.update({arg: result})
#         with open(f'{func.__name__}.json', 'w') as f:
#             json.dump(data, f, indent=4)
#         return result

#     return wrapper


# @our_cash
# def sum(one, two):
#     return one + two


# @our_cash
# def mult(one, two):
#     return one * two

# sum(3, 5)
# mult(1, 5)


'''
4. Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
'''

# def param(count: int):
#     def deco(func):
#         my_list = []
#         def wrapper(*args, **kargs):
#             for _ in range(count):
#                 result = func(*args, **kargs)
#                 my_list.append(result)
#             return my_list
#         return wrapper
#     return deco


# @param(3)
# def sum_(a, b):
#     return a + b

# print(sum_(2, 4))


'''
5.Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
декораторами для сохранения параметров,
декоратором контроля значений и
декоратором для многократного запуска.
Выберите верный порядок декораторов.
'''


from functools import wraps
import json

def our_cash(func: callable):
    try:
        with open(f'{func.__name__}.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        arg = str(args) + str(kwargs)
        data_res = data.get(arg)
        if data_res:
            return data_res
        result = func(*args, **kwargs)
        data.update({arg: result})
        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(data, f, indent=4)
            return result

    return wrapper

def param(count: int):
    def decor(func):
        my_list = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(count):
                result = func(*args, **kwargs)
                my_list.append(result)
            return my_list
        return wrapper
    return decor


@our_cash
@param(3)
def sum_(a, b):
    return a + b

print(sum_(6, 4))