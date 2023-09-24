'''
1. Создайте класс-функцию, который считает факториал числа при вызове экземпляра. 
Экземпляр должен запоминать последние k значений. 
Параметр k передаётся при создании экземпляра. 
Добавьте метод для просмотра ранее вызываемых чисел и их факториалов.
'''

# class MyFac:
#     def __init__(self, size: int):
#         self._size = size
#         self.__archiv: list = []

#     def show_archiv(self):
#         return self.__archiv

#     def __call__(self, namber: int):
#         res: int = 1
#         for i in range(1, namber+1):
#             res *= i

#         if len(self.__archiv) >= self._size:
#             self.__archiv.pop(0)
#         self.__archiv.append({namber: res})
#         return res


# if __name__ == '__main__':
#     f1 = MyFac(size=3)
#     print(f1(1))
#     print(f1(2))
#     print(f1(3))
#     print(f1(4))
#     print(f1(5))
#     print(f1(6))
#     print(f1(7))
#     print(f1.show_archiv())

'''
2. Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
'''

# import json

# class Factorial:

#     def __init__(self, k):
#         self.k = k

#         self.values = []

#     def __call__(self, num):
#         res = 1
#         for i in range(1, num + 1):
#             res *= i
#         if len(self.values) >= self.k:
#             self.values.pop(0)
#         self.values.append({num: res})
#         return res

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         with open(r'C:\Users\homei\OneDrive\Рабочий стол\DeepPythonLection\factorial.json', 'w', encoding='utf-8') as f:
#             json.dump(self.values, f)


# if __name__ == '__main__':

#     f = Factorial(4)
#     # print(f(5))
#     # print(f(6))
#     # print(f(7))
#     # print(f(8))
#     # print(f(9))
#     # print(f(10))
#     print(f.values)
#     with f as copy_:
#         print(copy_(3))
#         print(copy_(4))
#         print(copy_(5))
#         print(copy_(6))
#         print(copy_(7))
#         print(copy_(8))


'''
3. Создайте класс-генератор. 
Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step. 
Если переданы два параметра, считаем step=1. Если передан один параметр, также считаем start=1.
'''

# class Factorial:


#     def __init__ (self, *args):
#         if len(args) == 3:
#             self.start, self.stop, self.step = args
#         elif len (args) == 2:
#             self.start, self.stop = args
#             self.step = 1
#         elif len (args) == 1:
#             self.stop = args[0]
#             self.start = 1
#             self.step = 1


#     def __iter__ (self):
#         return self

#     def __next__ (self):
#         while self.start < self.stop:
#             res: int = 1
#             for i in range(1, self.start+1):
#                 res *= i
#             self.start +=1
#             return res
#         raise StopIteration

# if __name__ == "__main__":
#     a = Factorial(1,5,1)
#     for i in a:
#         print(i)


'''
4. Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
'''


# class Rectangle:
#     def __init__(self,
#                 length_cm: float,
#                 width_cm: float = None) -> None:
#         self.__length = length_cm
#         if width_cm:
#             self.__width = width_cm
#         else:
#             self.__width = length_cm

#     @property
#     def length(self):
#         return self.__length

#     @length.setter
#     def length(self, value):
#         if value < 0:
#             raise ValueError("не может быть меньше нуля")
#         self.__length = value

#     @property
#     def width(self):
#         return self.__width

#     @width.setter
#     def width(self, value):
#         if value < 0:
#             raise ValueError("не может быть меньше нуля")
#         self.__width = value


# if __name__ == '__main__':
#     r1 = Rectangle(length_cm= 2,
#     width_cm=3)
#     print(r1.length)
#     print(r1.width)
#     r1.length = 4
#     print(r1.length)
#     print(r1.width)
#     r1.length = 2
#     print(r1.length)
#     print(r1.width)


'''
5. Изменяем класс прямоугольника. 
Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
'''


class Side:

    def __init__(self, min_length, max_length):
        self.max_length = max_length
        self.min_length = min_length

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value):
        if not self.min_length < value < self.max_length:
            raise ValueError(f'Значение выходит за пределы заданных параметров.'
                             f' От {self.min_length} до {self.max_length}')

class Rectangle:

    __width = Side(0, 7)
    __length = Side(2, 10)

    def __init__(self,
                 length_cm: float,
                 width_cm: float = None) -> None:
        self.__length = length_cm
        if width_cm:
            self.__width = width_cm
        else:
            self.__width = length_cm

    def __repr__(self):
        return f'Rectangle(length_cm={self.__length}, ' \
               f'width_cm={self.__width})'

    def __str__(self):
        return f'Длинна: {self.__length}, ' \
               f'Ширина: {self.__width}.'



if __name__ == '__main__':
    r1 = Rectangle(length_cm=1,
    width_cm=3)
    print(r1)
    print(r1._Rectangle__length)