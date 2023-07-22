"""
3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
Пример:
Ввод:
1/2
1/3
Вывод:
5/6 1/6
"""

from fractions import Fraction

a = int(input('Введите числитель первой дроби: '))
b = int(input('Введите знаменатель первой дроби: '))
first_fraction = str(f'{a}/{b}')
new_first_fraction = Fraction(a, b)

c = int(input('Введите числитель второй дроби: '))
d = int(input('Введите знаменатель второй дроби: '))
second_fraction = str(f'{c}/{d}')
new_second_fraction = Fraction(c, d)

def sum_fraction(a, b, c, d):
    com_denominator = b*d
    a *= d
    c *= b
    sum = a + c
    if sum == com_denominator:
        print(1)
    else:
        for i in range(2, sum + 1):
            if sum % i == 0 and com_denominator % i == 0:
                sum /= i
                com_denominator /= i
        print(f'{sum}/{com_denominator}')

def product_fraction(a, b, c, d):
    multip_numenator = a*c
    multip_denominator = b*d
    if multip_numenator == multip_denominator:
        print(1)
    else:
        for i in range(2, multip_numenator + 1):  
            if multip_numenator % i == 0 and multip_denominator % i == 0:
                multip_numenator /= i
                multip_denominator /= i
        print(f'{multip_numenator}/{multip_denominator}')

print(first_fraction, second_fraction)

print('Выберите действие с дробями:\n'
      'введите "+" - сложение\n'
      'введите "*" - умножение')
action = input()
if action == '+':
    sum_fraction(a, b, c, d)
    print(new_first_fraction + new_second_fraction)
elif action == '*':
    product_fraction(a, b, c, d)
    print(new_first_fraction * new_second_fraction)
else:
    print('Не известная команда')
