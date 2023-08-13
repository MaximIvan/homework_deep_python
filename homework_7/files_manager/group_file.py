'''
функция для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''

import os
from pathlib import Path
import shutil
from files_manager.create_dir import create_dir

def group_file_in_dir(dir_source: str, dir_rezult: str):

    os.chdir("..")
    create_dir(dir_rezult)

    folder_track = Path(Path.cwd() / dir_source)         
    folder_move = Path(Path.cwd() / dir_rezult)          
    files = os.listdir(folder_track)  

    for items in files:
        extension = items.split('.')              

        if len(extension) > 1 and (
                extension[1].lower() == "jpg" or
                extension[1].lower() == "png" or
                extension[1].lower() == "svg"):
            file = str(folder_track) + '\\' + items                    
            new_path = str(folder_move) + "\\Photos\\" + items         
            print(new_path)
            create_dir(str(folder_move) + "\\Photos\\")               

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