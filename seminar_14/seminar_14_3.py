'''
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
'''
import pytest
from seminar_14 import clean_text


def test_one_clean_text():
    assert clean_text('Some text, тест') == 'some text, ', 'Тест один не пройден !'


def test_two_clean_text():
    assert clean_text('Hell456o worущшуd!') == 'hello word!', 'Тест два не пройден !'


def test_three_clean_text():
    assert clean_text('У меня есть подруга Anna! Ей 21 год.') == ' anna! .', 'Тест три не пройден'


if __name__ == '__main__':
    pytest.main(['-vv'])