'''
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
'''
import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(length_cm=2)
        self.r2 = Rectangle(length_cm=2, width_cm=4)
        self.r3 = Rectangle(length_cm=2)

    def test_step_1(self):
        self.assertEqual(self.r1, self.r3)

    def test_step_2(self):
        self.assertTrue(self.r1 == self.r3, 'Сравнение рабоет не корректно')


if __name__ == '__main__':
    unittest.main(verbosity=2)