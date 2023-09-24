'''
1. Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов. 
Возвращается строка в нижнем регистре.
'''

from string import ascii_letters, punctuation


def clean_text(text: str) -> str:
    """
    A function that removes characters from text other than Latin letters and spaces.
    >>> print(clean_text(text="Some text, тест"))
    some text,
    >>> print(clean_text(text="Привет Anna, сколько тебе лет?"))
     anna,   ? 
    """
    
    return "".join(i for i in text
                  if i in ascii_letters + punctuation + " ").lower()


print(clean_text(text="Some text, тест"))
print(clean_text(text="Привет Anna, сколько тебе лет?"))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

