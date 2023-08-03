'''
Создайте функцию генератор чисел Фибоначчи.
'''


def fib(number):
    a, b = 0, 1
    for _ in range(number):
        yield a
        a, b = b, a + b


num = int(input('введите число:  '))

print(list(fib(num)))