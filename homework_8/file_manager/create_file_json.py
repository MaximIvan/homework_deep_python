import json
import os
from pathlib import Path


def get_ids(filename)-> set:                                                    
    file = open(filename, 'r', encoding='utf-8')
    all_ids = set()
    try:                                                                
        data = json.load(file)                                                  
        for level in data:
            for uid in level:
                all_ids.add(uid)                                        
    except:
        pass
    file.close()
    return all_ids


def get_data(all_ids:set, filename):                                           
    working_dict = {}                                                         
    while True:
        name = input("введите имя: ")
        if name == "":
            break                                                              
        user_id = -1
        while user_id < 0 or user_id in all_ids:
            user_id = int(input("ввеедите id "))
        all_ids.add(user_id)                                                   

        access_level = 0
        while not 1 <= access_level <= 7:
            access_level = int(input('введите уровень доступа (1-7) '))
        if working_dict.get(access_level):                                  
            working_dict.get(access_level).update({user_id: name})              
        else:
            working_dict[access_level] = {user_id: name}
        fun_dump_json(working_dict, filename)                                      
        if input("продолжить ввод? y/n") != 'y':
            break


def fun_dump_json(working_dict, filename):                                        
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(working_dict, f)

def func(json_file: str):
    if not os.path.isfile(Path.cwd() / json_file):
        with open(json_file, 'w', encoding='utf-8') as f:
            f.write('')
        print(f'создан новый файл файл {json_file}')

    all_ids = get_ids(json_file)                                                  
    get_data(all_ids, json_file)                                      