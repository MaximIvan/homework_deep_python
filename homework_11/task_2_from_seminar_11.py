'''
2. Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса, 
старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов, 
которые также являются свойствами экземпляра.
'''


class Archiv:
    """
    Архив, который хранит пару свойств. При создании нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списков-архивов list-архивы также являются свойствами экземпляра
    """
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_int.append(cls.instance.number)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.old_text = []
            cls.instance.old_int = []
        return cls.instance

    def __init__(self, text: str, number: int) -> None:
        """
        init
        text: str
        number: int
        """
        self.text = text
        self.number = number

    def __repr__(self):
        return f'Archiv({self.text},{self.number})'


if __name__ == "__main__":
    a1 = Archiv(text='T', number=1)
    a2 = Archiv(text='E', number=2)
    a3 = Archiv(text='Z', number=3)

    print(a2.instance.old_text)
    print(a2.instance.old_int)

    print('---')

    print(a3.text)
    print(a3.number)

    print(Archiv.__doc__)
    print(Archiv.__init__.__doc__)

    print(a1.__repr__())
    print(a2.__repr__())
    print(a3.__repr__())