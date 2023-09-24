'''
1. Создайте класс МояСтрока где будут доступны все возможности str 
и дополнительно хранится имя автора строки и время создания (time.time)
'''

# import time


# class MyStr(str):
#     def __new__(cls, value: str, name: str):
#         instance = super().__new__(cls, value)
#         instance.name = name
#         instance.value = value
#         instance.time_create = time.time()
#         return instance

#     def __repr__(self):
#         return f'MyStr({self.value =}, {self.name =}, {self.time_create =})'


# if __name__ == "__main__":
#     str1 = MyStr(value="Это моя строка", name='Федор')
#     print(repr(str1))
#     print(str1.name)
#     print(str1.time_create)


'''
2. Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса, 
старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов, 
которые также являются свойствами экземпляра.
'''


# class Archiv:
#     instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.instance:
#             cls.instance.old_text.append(cls.instance.text)
#             cls.instance.old_int.append(cls.instance.number)
#         else:
#             cls.instance = super().__new__(cls)
#             cls.instance.old_text = []
#             cls.instance.old_int = []
#         return cls.instance

#     def __init__(self, text: str, number: int) -> None:
#         self.text = text
#         self.number = number


# if __name__ == "__main__":
#     a1 = Archiv(text='T', number=1)
#     a2 = Archiv(text='E', number=2)
#     a3 = Archiv(text='Z', number=3)

#     print(a2.instance.old_text)
#     print(a2.instance.old_int)

#     print('---')

#     print(a3.text)
#     print(a3.number)


'''
5. Дорабатываем класс прямоугольник из прошлого семинара. 
Добавьте возможность сложения и вычитания. 
При этом должен создаваться новый экземпляр прямоугольника. 
Складываем и вычитаем периметры, а не длинну и ширину. 
При вычитании не допускайте отрицательных значений.
'''

# class Rectangle:
#     def __init__(self,
#     length_cm: float,
#     width_cm: float = None) -> None:
#         self.length = length_cm
#         if width_cm:
#             self.width = width_cm
#         else:
#             self.width = length_cm

#     def calc_len(self):
#         return (self.width + self.length) * 2

#     def calc_square(self):
#         return self.width * self.length

#     def __add__(self, other):
#         return Rectangle(length_cm=
#         (self.length + other.length),
#         width_cm=self.width)

#     def __sub__(self, other):
#         return Rectangle(length_cm=
#         abs(self.length - other.length),
#         width_cm=self.width)


# if __name__ == '__main__':
#     r1 = Rectangle(length_cm=2,
#     width_cm=2)
#     print(f'{r1.calc_len() = }')
#     print(f'{r1.calc_square() = }')
#     print('---')

#     r2 = Rectangle(length_cm=3)
#     print(f'{r2.calc_len() = }')
#     print(f'{r2.calc_square() = }')

#     r3 = r2 + r1

#     print('---')
#     print(f'{r3.calc_len() = }')
#     print(f'{r3.calc_square() = }')



'''
6. Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
'''

class Rectangle:
    def __init__(self,
                length_cm: float,
                width_cm: float = None) -> None:
        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm

    def calc_len(self):
        return (self.width + self.length) * 2

    def calc_square(self):
        return self.width * self.length

    def __add__(self, other):
        return Rectangle(length_cm=
                        (self.length + other.length),
                        width_cm=self.width)

    def __sub__(self, other):
        return Rectangle(length_cm=
                        abs(self.length - other.length),
                        width_cm=self.width)

    def __eq__(self, other: "Rectangle"):
        return self.calc_square() == other.calc_square()

    def __lt__(self, other: "Rectangle"):
        return self.calc_square() < other.calc_square()

    def __gt__(self, other: "Rectangle"):
        return self.calc_square() > other.calc_square()

    def __ge__(self, other: "Rectangle"):
        return self.calc_square() >= other.calc_square()

    def __le__(self, other: "Rectangle"):
        return self.calc_square() <= other.calc_square()


if __name__ == '__main__':
    r1 = Rectangle(length_cm=2,
    width_cm=2)
    print(f'{r1.calc_len() = }')
    print(f'{r1.calc_square() = }')
    print('---')

    r2 = Rectangle(length_cm=3)
    print(f'{r2.calc_len() = }')
    print(f'{r2.calc_square() = }')

    r3 = r2 + r1

    print('---')
    print(f'{r3.calc_len() = }')
    print(f'{r3.calc_square() = }')

    print(r1 == r2)
    print(r1 <= r2)
    print(r1 >= r2)