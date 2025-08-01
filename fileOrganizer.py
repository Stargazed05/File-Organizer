#
# small script for organizing files in a directory
#
import os
import shutil
from tkinter import filedialog
from tkinter import Tk
#comment for tests

def dict_maker(lines):
    result = {}
    current_key = None

    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue

        if current_key is None:
            current_key = stripped_line[:-1]
        else:
            result[current_key] = stripped_line
            current_key = None
    return result


def empty_fol_rem(target_dir):
    dir_list = os.listdir(target_dir)
    for obj in dir_list:
        try:
            os.rmdir(target_dir + "/" + obj)
        except OSError:
            print(obj + " is not a empty folder")


file_name = open("file_extensions_by_category.txt")
extension_dict = dict_maker(file_name)

selected_destiny = None
Tk().withdraw()
selected_path = filedialog.askdirectory(title='Select Files Directory')

if selected_path == '':
    print("Path wasn't chosen, aborting...")
else:
    Tk().withdraw()
    selected_destiny = filedialog.askdirectory(title='Select Files Destiny')

files_to_move = os.listdir(selected_path)
print("your chosen path is: " + selected_path)

moved_files_number = 0

for key, value in extension_dict.items():
    print(f'Searching: {key}')
    for file_name in files_to_move:
        suffix = file_name.split(sep=".")
        files_type_counter = 0
        if suffix[-1].lower() in extension_dict[key].lower():
            try:
                if os.path.isdir(key):
                    shutil.move(file_name, f'/{key}')
                else:
                    try:
                        os.makedirs(selected_path + "/" + key)
                        shutil.move(selected_path + f'/{file_name}', selected_destiny + f'/{key}')
                        moved_files_number += 1
                    except FileExistsError:
                        shutil.move(selected_path + f'/{file_name}', selected_destiny + f'/{key}')
                        moved_files_number += 1
            except FileNotFoundError:
                print(f'File: {file_name} not found. Continuing through')
        else:
            pass

empty_fol_rem(selected_destiny)
print(f'Done! {moved_files_number} Files moved and organized to {selected_destiny}.')
