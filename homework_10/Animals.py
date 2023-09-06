class Animal:
    def __init__(self, name: str, age: int):
        self.name = name.capitalize()
        self.age = age

    def get_info(self) -> str:
        return (f'{"Class:":8}{type(self).__name__}'
                f'\n{"Name:":8}{self.name}'
                f'\n{"Age:":8}{self.age} years')


class Bird(Animal):

    def __init__(self, name: str, age: int, color: str, voice: str):
        super().__init__(name, age)
        self.color = color
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":8}{self.color}'
                f'\n{"Voice:":8}{self.voice}\n'
                )


class Fish(Animal):

    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":8}{self.color}\n'
                )
    
class Dog(Animal):
    def __init__(self, name: str, age: int, color: str, voice: str, is_domestic: bool):
        super().__init__(name, age)
        self.color = color
        self.voice = voice
        self.is_domestic = is_domestic

    def get_specific(self):
        if self.is_domestic:
            return f'домашняя'
        return f'дворняга'
    
    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":8}{self.color}'
                f'\n{"Voice:":8}{self.voice}' 
                f'\n{"Home:":8}{self.get_specific()}'
                )


if __name__ == '__main__':
    bird = Bird('ворон', 2, "серая", "kar-kar")
    dog = Dog('стив', 1, 'белый с коричневыми пятнышками', 'гав-гав', True)
    print(f' {bird.name = }, {bird.age = }, {bird.voice = }, {bird.color = }, {bird.get_info()}')
    print(f' {dog.name = }, {dog.age = }, {dog.voice = }, {dog.color = }, {dog.get_specific()}, {dog.get_info()}')