import os
from os import rename
import shutil

path = "C:\image"
file_list = os.listdir(path)
print(file_list)


def make_copies(file_name, dest_directory):
    f = file_name
    dir_url = "C:\image/"
    files = os.listdir(dir_url)
    numlist = []
    for i in range(1, 30):
        numlist.append(i)

    source_file = (path + "/" + f)
    shutil.copy(source_file, dest_directory)
    for j in numlist:
        rename(dir_url + f, dir_url + f.replace(str(j), str(j + 1)))
        f = f.replace(str(j), str(j + 1))
        source_file = (path + "/" + f)
        shutil.copy(source_file, dest_directory)
        last = j + 1
    rename(dir_url + f, dir_url + f.replace(str(j+1), str(1)))

for i in file_list:
    dir_path = "C:\images"
    file_name = i
    dir_name = file_name[:-4]
    os.mkdir(dir_path + "/" + dir_name + "/")
    dest_directory = (dir_path + "/" + dir_name + "/")
    make_copies(file_name, dest_directory)
