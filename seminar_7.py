'''
1. Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. Первое число int, второе - float разделены вертикальной чертой. Минимальное число - -1000, максимальное - +1000. Количество строк и имя файла передаются как аргументы функции.
'''

# from random import randint, uniform


# def write_file_random(filename: str, count_lines: int) -> None:
#     with open(filename, 'w', encoding='utf-8') as f:
#         for i in range(count_lines):
#             int_num = randint(-1000, 1000)
#             float_num = uniform(-1000, 1000)
#             f.write(f'{int_num:>5} | {float_num:.2f}\n')


# if __name__ == '__main__':
#     write_file_random('task_1.txt', 20)


'''
2. Напишите функцию, которая генерирует псевдоимена. Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные. Полученные имена сохраните в файл.
'''

# import random
# from random import randint

# VOLEWELS = 'аеиоуяюёэы'     # гласные русские буквы
# # CONSONANTS = (chr(char) for char in range(ord('а'), ord('я') + 1) if chr(char) not in VOLEWELS)   # согласные русские буквы в виде генератора, тогда print(*CONSONANTS)
# CONSONANTS = ''.join([chr(char) for char in range(ord('а'), ord('я') + 1) if chr(char) not in VOLEWELS])    # согласные русские буквы в виде списка, тогда print(CONSONANTS)


# def make_random_name(amount_of_names: int):

#     #
#     count = 0
#     all_names = []

#     while count != amount_of_names:
#         word_len = randint(4, 7)
#         word = random.choices(VOLEWELS + CONSONANTS, k=word_len)
#         if any(ch in VOLEWELS for ch in word):          # если есть хотя бы одна гласная в слове
#             all_names.append(''.join(word).capitalize() + '\n')
#             count += 1
#     with open('task_2.txt', 'a', encoding='utf-8') as f:
#         f.writelines(all_names)

# if __name__ == '__main__':
#     make_random_name(10)


'''
3. Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами. Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле. При достижении конца более короткого файла, возвращайтесь в его начало.
'''

# def whatever():
#     with (open('task_1.txt', 'r', encoding='utf-8') as f_numbers,
#           open('task_2.txt', 'r', encoding='utf-8') as f_names):
#         numbers = f_numbers.readlines() #['  -819 | 936.48\n', ' 916 | -817.09\n', ' 169 | -153.08\n', '  - 566 | -428.04
#         names = f_names.readlines()     #['Вгбэеъ\n',  'Яикч\n', 'Вярщмт\n', 'Ыюзбцф']

#     lines_to_write = []
#     length_of_longest = max(len(numbers), len(names))

#     for i in range(length_of_longest):
#         num = numbers[i % len(numbers)]
#         a, b = map(float, num.split('|'))       # a=-945   b=875.661
#         mult = a * b

#         name = names[i % len(names)]
#         if mult >= 0:
#             lines_to_write.append(f'{name.upper().rstrip()}; {round(mult)}\n')  # .rstrip() - убирает справа пробелы
#         else:
#             lines_to_write.append(f'{name.lower().rstrip()}; {abs(mult)}\n')

#     with open ("task_3.txt", 'w', encoding='utf-8')as f:
#         f.writelines(lines_to_write)

# if __name__ == '__main__':
#     whatever()


'''
4. Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
'''

from string import ascii_letters    # все буквы латинские abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
from random import randint, choices, randbytes




def create_file(extension: str, min_len_name: int = 2, max_len_name: int = 5,
                min_size_file: int = 256, max_size_file: int = 4096, amount_file: int = 5) -> None:
    for _ in range(amount_file):
        len_name = randint(min_len_name, max_len_name)
        #file_name = choices(ascii_letters, k=len_name)  возвращает список  рандомных значений букв
        file_name = ''.join(choices(ascii_letters, k=len_name)) + extension # возвращает строку имя файла с расширением
        size = randint(min_size_file, max_size_file)
        with open(file_name, 'wb') as f:
            f.write(randbytes(size))

# if __name__ == '__main__':
#     create_file('.txt')


'''5.
✔ Доработаем предыдущую задачу. 
✔ Создайте новую функцию которая генерирует файлы с разными расширениями. 
✔ Расширения и количество файлов функция принимает в качестве параметров. 
✔ Количество переданных расширений может быть любым. 
✔ Количество файлов для каждого расширения различно. 
✔ Внутри используйте вызов функции из прошлой задачи.
'''


def gen_files(data: dict):
    for key, value in data.items():
        create_file(key, amount_file=value)

if __name__ == '__main__':
    my_dict = {'.txt':2, '.doc':2, '.bin': 2, '.pdf': 2}
    gen_files(my_dict)



'''
6. Дорабатываем функции из предыдущих задач. Генерируйте файлы в указанную директорию - отдельный параметр функции. Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки). Существующие файла не должны удаляться/изменяться в случае совпадения имён.
'''


from pathlib import Path
import os


def create_dir(name_dir: str):
    #name = Path(name_dir)   # new
    #path = name.cwd() / name_dir  
    name = Path(Path.cwd() / name_dir)
    if not name.exists():       #проверка на наличие директория
        name.mkdir()            #создает директорий с именем name_dir в текущем директории

    os.chdir(name)          #переходим в созданный каталог сделав его текущим


if __name__ == '__main__':
    my_dict = {'.txt': 1, '.doc': 1, '.bin': 1, '.pdf': 1}
    gen_files(my_dict)
    create_dir('new')


'''
7. Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. Каждая группа включает файлы с несколькими расширениями. В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''

import os
from pathlib import Path
import shutil


def group_file_in_dir(dir_source: str, dir_rezult: str):

    os.chdir("..")
    create_dir(dir_rezult)

    folder_track = Path(Path.cwd() / dir_source)         
    folder_move = Path(Path.cwd() / dir_rezult)         

    files = os.listdir(folder_track)  # список всех файлов директория

    for items in files:
        extension = items.split('.')                #список имени + расширения


        if len(extension) > 1 and (
                extension[1].lower() == "jpg" or
                extension[1].lower() == "png" or
                extension[1].lower() == "svg"):
            file = str(folder_track) + '\\' + items                     #путь файла в исходном директории
            new_path = str(folder_move) + "\\Photos\\" + items          #путь файла в новом директории
            print(new_path)
            create_dir(str(folder_move) + "\\Photos\\")                 # создаем новый директорий под группу файлов

            shutil.move(file, new_path)
        elif len(extension) > 1 and (extension[1].lower() == 'avi' or
                                     extension[1].lower() == 'mpg' or
                                     extension[1].lower() == 'gif' or
                                     extension[1].lower() == 'mp4' or
                                     extension[1].lower() == 'mpeg' or
                                     extension[1].lower() == 'mpg' or
                                     extension[1].lower() == 'flac'):
            file = str(folder_track) + "\\" + items
            new_path = str(folder_move) + "\\Videos\\" + items
            create_dir(str(folder_move) + "\\Videos\\")
            shutil.move(file, new_path)
        elif len(extension) > 1 and (extension[1].lower() == 'torrent'):
            file = str(folder_track) + "\\" + items
            new_path = str(folder_move) + "\\Torrent\\" + items
            create_dir(str(folder_move) + "\\Torrent\\")
            shutil.move(file, new_path)
        elif len(extension) > 1 and (extension[1].lower() == 'rar' or
                                     extension[1].lower() == 'zip' or
                                     extension[1].lower() == 'jar'):
            file = str(folder_track) + "\\" + items
            new_path = str(folder_move) + "\\Archive\\" + items
            create_dir(str(folder_move) + "\\Archive\\")
            shutil.move(file, new_path)

if __name__ == '__main__':
    group_file_in_dir('new', 'rezult')


# еще вариант решения:


# from os import chdir, listdir, mkdir, getcwd
# from pathlib import Path

# def sort_files(directory: str | Path = 'test_dir'):
# chdir(directory)
# print(listdir())
# for file in Path(getcwd()).iterdir():
# if file.is_dir():
# continue
# ext = file.name.split('.')[1]
# if ext.upper() not in listdir():
# mkdir(ext.upper())
# file.replace(f"{ext.upper()}\\{file.name}")