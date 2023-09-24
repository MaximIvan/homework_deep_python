"""
2. Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
порядковый номер начиная с единицы
значение
адрес в памяти
размер в памяти
хэш объекта
результат проверки на целое число только если он положительный
результат проверки на строку только если он положительный Добавьте в список повторяющиеся элементы и сравните на результаты.
"""

# data = ['vvv', 12, 12.01, 'kkk', (12, )]
# for num, element in enumerate(data, start=1):
#     if isinstance(element, int):
#         elem_type = 'INT'
#     elif isinstance(element, str):
#         elem_type = 'STR'
#     print(f"""{num} {element} {id(element)}
# {element.__sizeof__()} {hash(element)} {elem_type} {type(element)}""")
#     print()


"""
3. Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление. Функции bin и oct используйте для проверки своегорезультата, а не для решения. Дополнительно: Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления. Избегайте магических чисел. Добавьте аннотацию типов где это возможно
"""

# BIN_DIV = 2
# OCT_DIV = 8
# num = 10
# process_num = num
# res = ''

# while process_num > 0:
#     res += str(process_num % BIN_DIV)
#     process_num //= BIN_DIV

# res = res[::-1]
# print(res, bin(num))

# while process_num > 0:
#     res += str(process_num % OCT_DIV)
#     process_num //= OCT_DIV

# res = res[::-1]
# print(res, oct(num))


"""
4. Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру. Диаметр не превышает 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.
"""

# from math import pi
# import decimal

# decimal.getcontext().prec = 44

# diam = decimal.Decimal(10)
# pi_ = decimal.Decimal(pi)

# square = (pi_*diam**2)/4
# length = pi_*diam

# print(pi_)
# print((square, length))


"""
5. Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный. Используйте комплексные числа для извлечения квадратного корня.
"""

# a = 1
# b = -6
# c = 34

# d = b**2 - 4*a*c

# if d != 0:
#     x1 = (-b + d**0.5)/(2*a)
#     x2 = (-b - d**0.5)/(2*a)
#     result = 'уравнение имеет 2 корня: х1=' + str(x1) + ' x2=' + str(x2)
# else:
#     x = (-b)/(2*a)
#     result = 'уравнение имеет 1 корень: х=' + str(x)
# print(result)

"""
6. Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег
"""

COMM_WITHDRAWAL = 1.5
COMM_REFIL = 3
TAX = 10
COMM_MIN = 30
COMM_MAX = 600
SUM_WORK = 50
MAX_COUNT = 5_000_000
account = 0
count_refil = 0
count_withdrawal = 0

def get_money(input_string:str)->int:
    while True:
        try:
            num = int(input(input_string))
            if num > 0 and num % SUM_WORK == 0:
                return num
            else:
                print('Сумма должна быть положительной и кратной 50')
        except ValueError:
            print('Это не то...')

def refil_account(num:int):
    global account 
    account += num

def account_proc():
    num = account/100*COMM_REFIL
    refil_account(num)

def take_account(num:list):
    global account 
    account -= num

def take_tax():
    if account > MAX_COUNT:
        num = account/100*TAX
        take_account(num)

def chek_money(num):
    proc = num/100*COMM_WITHDRAWAL
    if proc < COMM_MIN:
        num += COMM_MIN
    elif proc > COMM_MAX:
        num += COMM_MAX
    else:
        num += proc
    return num

print('Здравствуйте. Это программа банкомат\n')
while True:
    choice = int(input('Выберите действие:\n'
        '1 - пополнить счет\n'\
        '2 - снять деньги со счета\n'
        '3 - выход\n'))
    match choice:
        case 1:
            number = get_money('Введите сумму для зачисления на счет:\n')
            take_tax()
            refil_account(number)
            count_refil += 1
            if count_refil == 3:
                account_proc()
                count_refil = 0
            print(f'У вас на счету: {account} рублей')
        case 2:
            number = get_money('Введите сумму для снятия со счета:\n')
            take_tax()
            number = chek_money(number)
            if number < account:
                take_account(number)
                count_withdrawal += 1
                if count_withdrawal == 3:
                    account_proc()
                    count_withdrawal = 0
            else:
                print('Недостаточно средств')
            print(f'У вас на счету: {account} рублей')
        case 3:
            print('До свидания')
            print(f'У вас на счету: {account} рублей')
            break
        case _:
            print('Не известная команда')




