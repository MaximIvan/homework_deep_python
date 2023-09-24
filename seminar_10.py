'''
1. Создайте класс окружность. Класс должен принимать радиус окружности при создании экземпляра. 
У класса должно быть два метода, возвращающие длину окружности и её площадь.
'''


# import math


# class Circle:
#     _pi = math.pi

#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def calc_len(self):
#         return self._pi * self.radius * 2

#     def calc_area(self):
#         return self._pi * self.radius ** 2


'''
2. Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра. 
У класса должно быть два метода, возвращающие периметр и площадь. 
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
'''


# class Rectangle:
#     def __init__(self, length: float, width: float = None) -> None:
#         self.length = length
#         if width:
#             self.width = width
#         else:
#             self.width = length

#     def calc_len(self):
#         return (self.width + self.length) * 2

#     def calc_area(self):
#         return self.width * self.length


# if __name__ == '__main__':
#     r1 = Rectangle(length=2, width=2)
#     print(f'{r1.calc_len() = }')
#     print(f'{r1.calc_area() = }')

#     print('---')

#     r2 = Rectangle(length=3)
#     print(f'{r2.calc_len() = }')
#     print(f'{r2.calc_area() = }')

'''
3. Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 
У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор. 
Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.
'''


# class Person:
#     def __init__(self, surname, name, patronymic, age):
#         self.surname = surname
#         self.name = name
#         self.patronymic = patronymic
#         self.__age = age

#     def get_age(self):
#         return self.__age

#     def birthday(self):
#         self.__age += 1

#     def __str__(self):
#         return f'{self.surname} {self.name} {self.patronymic}'

# if __name__ == '__main__':
#     p1 = Person("Ivanov", 'Ivan', 'Ivanovich', 25)
#     #print(p1.__age)
#     print(p1.get_age())
#     print(p1.name)
#     print(p1)
#     p1.birthday()
#     print(p1.get_age())


'''
4. Создайте класс Сотрудник. Воспользуйтесь классом человека из прошлого задания. 
У сотрудника должен быть шестизначный идентификационный номер и уровень доступа (остаток от суммы цифр id делённой на семь).
'''


# import random


# def sum_didgit(a: int): # функцию для определения уровнея доступа задали вне класса, т.к. класс не может обращаться 
#     a = str(a)          # к самому себе при инициализации
#     sum_a = 0
#     for i in a:
#         sum_a += int(i)
#     return sum_a % 7

#класс Person взял из прошлой задачи

# class Employ(Person):
#     def __init__(self, surname, name, patronymic, age):
#         super().__init__(surname, name, patronymic, age)   #super используем для перетаскивания из родительского класса необходимых нам полей
#         self.id = random.randint(100000, 999999)
#         self.level = sum_didgit(self.id)

# if __name__ == '__main__':
#     p1 = Employ("Ivanov", 'Ivan', 'Ivanovich', 25)
#     print(p1)
#     print(p1.get_age())
#     print(p1.id, p1.level)


'''
5. Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
'''


# class Animal:
#     def __init__(self, name, age):
#         self.__name, self.__age = name, age

#     def get_name(self):
#         return self.__name.capitalize()

#     def get_age(self):
#         return self.__age


# class Fish(Animal):

#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.__color = color

#     def get_specific(self):
#         return self.__color


# class Mammal(Animal):
#     def __init__(self, name, age, wool):
#         super().__init__(name, age)
#         self.__wool = wool

#     def get_specific(self):
#         return self.__wool


# class Bird(Animal):
#     def __init__(self, name, age, feather):
#         super().__init__(name, age)
#         self.__feather = feather

#     def get_specific(self):
#         return self.__feather



# class Dog(Animal):
#     def __init__(self, name, age, is_domestic):
#         super().__init__(name, age)
#         self.is_domestic = is_domestic

#     def get_specific(self):
#         if self.is_domestic:
#             return f'домашняя'
#         return f'дворняга'

#     # def __str__(self):
#     #     if self.is_domestic:
#     #         return f'Dog {self.__name} домашняя'
#     #     return f'Dog {self.__name} дворняга'
    
# if __name__ == '__main__':
#     dog = Dog('stive', 1, True)
#     print(f'имя собаки: {dog.get_name()}, возраст: {dog.get_age()}, принадлежность: {dog.get_specific()}')
#     bird = Bird("ворон", 2, "черные")
#     print(f'имя птицы: {bird.get_name()}, возраст {bird.get_age()}, оперенье {bird.get_specific()}')
#     print('-----------------------')
#     print(dog)
#     print(bird)


'''
от преподавателя
'''

class Animal:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    def __str__(self) -> str:
        return f'{self.name} {self.age}'

    def birthday(self):
        self.age += 1


class Dog(Animal):
    def __init__(self,
    name: str,
    age: int,
    color: str,
    breed: str,
    is_domestic: bool = True) -> None:
        super().__init__(name, age)

        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic

    def __str__(self):
        if self.is_domestic:
            return f'Dog {self.color} {self.breed} домашняя'
        return f'Dog {self.color} {self.breed} дворняга'


class Kotopes(Animal):
    def __init__(self,
        age: int,
        name: str,
        number_heads: int = 2) -> None:
        super().__init__(name, age)
        self.__number_heads = number_heads

    def __str__(self):
        return f'Kotopes -> number_heads: {self.__number_heads},\
                Возраст: {self.age}, не женат '


class Fish(Animal):

    def __init__(self, name, age, aqua, size):
        super().__init__(name, age)
        self.aqua = aqua
        self.size = size

    def __str__(self):
        if self.aqua:
            return f'{self.name} морская'
        else:
            return f'{self.name} пресноводная'


if __name__ == "__main__":
    dog = Dog('Бобик', 3, "рыжий", "спаниель", True)
    dog2 = Dog('Тузик', 4, "серый", "спаниель", False)
    f1 = Fish("Дори", 1, True, 0.5)
    kt1 = Kotopes(3, "котопес", 2)
    print(dog)
    print(f1)
    print(kt1)
    kt1.birthday()
    print(kt1)
