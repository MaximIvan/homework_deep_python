# Task 1.
# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию,
# которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.
import json


def txt_to_json(input_filename: str,
                output_filename: str):

    with open(input_filename, 'r', encoding='utf-8') as f:
        data = f.read().split('\n')[:-1]
    data = [{i.split(';')[0].capitalize():
        float(i.split()[1])} for i in data]

    with open(output_filename, 'w', encoding='utf-8') as res:
        json.dump(data, res, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    txt_to_json('task_3.txt', 'sem8_output.json')


'''
Task 2.
Напишите функцию,
которая в бесконечном цикле запрашивает имя,
личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
'''

# import json


# def uniq_id(data: dict, id: str) -> bool:
#     for item in data.values():
#         if id in item.keys():
#             return False
#     return True


# def add_user(fname: str) -> None:
#     fname += '.json'
#     while True:
#         id = input('id: ')
#         name = input('name: ')
#         level = input('level: ')

#         try:
#             with open(fname, 'r', encoding='UTF-8') as fr:
#                 new_dict: dict = json.load(fr)
#         except:
#             new_dict: dict = {str(i): {} for i in range(1, 8)}

#         if uniq_id(new_dict, id):
#             new_dict[level].update({id: name})
#         else:
#             print('не уникальный id')
#             continue

#         with open(fname, 'w', encoding='UTF-8') as fw:
#             json.dump(new_dict, fw, indent=2)


# if __name__ == '__main__':
#     add_user(fname='users')


'''
Task 3.
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
'''
# import json
# import csv


# def json_to_csv(filename: str):
#     with open(f'{filename}.json', 'r') as f_inp:
#         data = json.load(f_inp)
#     rows = []
#     for level, users in data.items():
#         for id, name in users.items():
#             rows.append({'level': level,
#                          'name': name,
#                          'id': id})
#     with open(f'{filename}.csv', 'w', newline='') as res:
#         csv_write = csv.DictWriter(res, fieldnames=['level',
#                                                     'name',
#                                                     'id'])
#         csv_write.writeheader()
#         csv_write.writerows(rows)


# if __name__ == '__main__':
#     json_to_csv('users')

'''
Task 4.
Прочитайте созданный в прошлом задании
csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл,
где каждая строка csv файла представлена как
отдельный json словарь.
Имя исходного и конечного файлов
передавайте как аргументы функции.
'''

# import json
# import csv


# def csv_to_json(filename: str):
#     with open(f'{filename}.csv', 'r', newline='') as f_csv:
#         data = f_csv.read().split('\n')
#         print(data)

#     res: list = []
#     data.pop()
#     for value in data[1:]:
#         print(value)
#         level, name, id = value[:-1].split(',')
#         res.append({"id": f"{int(id):06}", "level": level, "name": name, "hash": hash(id+name)})

#     with open(f'task5_{filename}.json', 'w', newline='') as f_json:
#         json.dump(res, f_json, indent=4)


# if __name__ == '__main__':
#     csv_to_json('users')

'''
Task 6.
Напишите функцию, которая ищет json файлы в указанной директории
и сохраняет их содержимое в виде одноимённых pickle файлов.
'''
import json
import pickle
import os


def json_to_pikle(dir: str = '2108'):
    files = list(filter(lambda x: '.json' in x, os.listdir()))
    for file in files:
        filename, *_ = file.split('.')
        with (open(file, 'r') as source,
        open(f'{filename}.pickle', 'wb') as res):
            data = json.load(source)
            pickle.dump(data, res)


if __name__ == "__main__":
    json_to_pikle()

