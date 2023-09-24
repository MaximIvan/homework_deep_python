# Task 5

# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

# n = 21
# e = 4

# i = 0
# sum_even = 0

# while i <= n:
#     i += 1
#     if i % e == 0 or i % 2 != 0:
#         continue
#     sum_even += i

# print(sum_even)

# Task 6

# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

# MAIN_LEAP_CRITERIA = 4
# EXCEPT_LEAP_CRIT = 100
# ADDITIONAL_LEAP_CRIT = 400

# year = int(input('Year: '))

# if (year % MAIN_LEAP_CRITERIA == 0 and year % EXCEPT_LEAP_CRIT != 0) or (year % ADDITIONAL_LEAP_CRIT == 0):
#     print('Год високосный')
# else:
#     print('Не является високосным')

# Task 7

# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

# NUM = input('Введите число ')
# NUM_NEW = int(NUM)
# COUNTER = 0

# while NUM_NEW != 0:
#     NUM_NEW //= 10
#     COUNTER += 1

# if COUNTER == 3:
#     verdict = 'трёхзначное'
#     result = NUM[::-1]
# elif COUNTER == 2:
#     verdict = 'двузначное'
#     result = int(NUM[0]) * int(NUM[1])
# elif COUNTER == 1:
#     verdict = 'цифра'
#     result = int(NUM)**2


# print(f'{verdict} | {result}')

# Task 8

# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********


NUM_OF_ROWS = int(input('Сколько рядов у ёлки? '))

STAR = '*'
SPACE = " "
DIVEDER = 2

SPACE_COUNT = ((NUM_OF_ROWS * DIVEDER) - DIVEDER) // DIVEDER
STARS_COUNT = 1
for i in range(NUM_OF_ROWS):
    print(SPACE * (SPACE_COUNT - i)
          + STAR * (STARS_COUNT + DIVEDER * i)
          + SPACE * (SPACE_COUNT - i))