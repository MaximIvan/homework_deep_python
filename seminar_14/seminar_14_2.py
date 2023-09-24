'''
Напишите для задачи 1 тесты unittest.
Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
'''

import unittest
from seminar_14 import clean_text




class TestCleanText(unittest.TestCase):
    def test_one_clean_text(self):
        self.assertEqual(clean_text('Some text, тест'), 'some text, ')

    def test_two_clean_text(self):
        self.assertEqual(clean_text('Hell456o worущшуd!'), 'hello word!')

    def test_three_clean_text(self):
        self.assertEqual(clean_text('У меня есть подруга Anna! Ей 21 год.'), '    anna!   .', msg= 'Что то пошло не так ...')



if __name__ == '__main__':
    unittest.main(verbosity=2)

