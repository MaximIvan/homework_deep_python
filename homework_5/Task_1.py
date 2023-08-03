'''
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

import os


def take_string(file_path: str) -> tuple:
    path, file_name = os.path.split(file_path)
    name, extension = file_name.split('.')
    return path, name, extension

string = "C:/Users/homei/OneDrive/Рабочий стол/DeepPythonLection/seminar_1.py"

print(f'Путь к файлу: {string} \nПолученный кортеж: {take_string(string)}')

