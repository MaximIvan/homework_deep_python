'''
6. Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
'''

class Rectangle:
    def __init__(self,
                length_cm: float,
                width_cm: float = None) -> None:
        """
        init
        length_cm: float
        width_cm: float
        """
        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm

    def calc_len(self):
        '''
        Нахождение периметра
        '''
        return (self.width + self.length) * 2

    def calc_square(self):
        '''
        Нахождение площади
        '''
        return self.width * self.length

    def __add__(self, other):
        '''
        add 
        new object
        '''
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
    print(Rectangle.__init__.__doc__)
    r1 = Rectangle(length_cm=2,
    width_cm=2)
    print(Rectangle.calc_len.__doc__)
    print(f'{r1.calc_len() = }')
    print(Rectangle.calc_square.__doc__)
    print(f'{r1.calc_square() = }')
    print('---')


    r2 = Rectangle(length_cm=3)
    print(f'{r2.calc_len() = }')
    print(f'{r2.calc_square() = }')

    r3 = r2 + r1

    print('---')
    print(Rectangle.__add__.__doc__)
    print(f'{r3.calc_len() = }')
    print(f'{r3.calc_square() = }')

    print(r1 == r2)
    print(r1 <= r2)
    print(r1 >= r2)

