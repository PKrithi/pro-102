import os
import shutil
from_dir = "c:/users/admin/notes"
to_dir = "c://users/download_images"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name, extension = os.path.split_text(file_name)
    print(list_of_files)
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path_one = from_dir + '/' + file_name
        path_two = to_dir + '/' + "image_files"
        path_three = to_dir + '/' + "image_files" + file_name
        if os.path.exists(path_two):
            shutil.move(path_one, path_three)
        else:
            os.mk_dirs(path_two)
            shutil.move(path_one, path_three)