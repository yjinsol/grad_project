import os
import shutil

path = "C:\kkk"
file_list = os.listdir(path)
print(file_list)

for i in file_list:
    dir_path = "C:\ddd"
    file_name = i
    dir_name = file_name[:-4]
    os.mkdir(dir_path + "/" + dir_name + "/")
    dest_directory = (dir_path + "/" + dir_name + "/")
    source_file = (path + "/" + file_name)
    shutil.copy(source_file, dest_directory)









#print ("file_list: {}".format(file_list))

