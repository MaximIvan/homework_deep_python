from files_manager.create_dir import create_dir
from files_manager.gen_files import gen_files
from files_manager.group_file import group_file_in_dir
from files_manager.group_rename import group_rename



if __name__ == '__main__':

    create_dir('new')                             

    my_dict = {'.txt': 2, '.zip': 1,
               '.rar': 1, '.avi': 2,
               '.mp4': 2, '.pop': 2,
               '.gif': 2, '.mpeg': 2,
               '.jpg': 2}
    gen_files('new', my_dict)                    
    group_file_in_dir('new', 'rezult')             
    group_rename(4, 'pip', 'zip', [2, 4], "new")  