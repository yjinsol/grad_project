import os
from os import rename
import shutil

def make_copies(file_name, dest_directory):
    f = file_name
    dir_url = "C:\wooribank_url/"
    files = os.listdir(dir_url)
    numlist = []
    for i in range(1, 30):
        numlist.append(i)

    source_file = (path + "/" + f)
    shutil.copy(source_file, dest_directory)

    rename(dir_url + f, dir_url + f.replace(".png", "1.png"))
    f = f.replace(".png", "1.png")
    source_file = (path + "/" + f)
    shutil.copy(source_file, dest_directory)

    for j in numlist:
        rename(dir_url + f, dir_url + f.replace("{0}.png".format(j), "{0}.png".format(j+1)))
        f = f.replace("{0}.png".format(j), "{0}.png".format(j+1))
        print(f)
        source_file = (path + "/" + f)
        shutil.copy(source_file, dest_directory)
        last = j+1
    rename(dir_url + f, dir_url + f.replace("{0}.png".format(j+1), ".png"))

path = "C:\wooribank_url"
file_list = os.listdir(path)
print(file_list)


for i in file_list:
    dir_path = "C:\wooribank_url_copies"
    file_name = i
    dir_name = file_name[:-4]
    os.mkdir(dir_path + "/" + dir_name + "/")
    dest_directory = (dir_path + "/" + dir_name + "/")
    make_copies(file_name, dest_directory)

