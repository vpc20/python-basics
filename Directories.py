import os
from os.path import isdir, join


def list_dir_recursive(path):
    try:
        dir_list = os.listdir(path)
    except WindowsError:
        pass

    for dir_entry in dir_list:
        complete_dir_entry = join(path, dir_entry)
        if isdir(complete_dir_entry):
            list_dir_recursive(complete_dir_entry)
        else:
            print(complete_dir_entry)  # print filenames


def list_dir_iterative(path):
    dir_queue = [path]
    while dir_queue:
        path = dir_queue.pop(0)
        try:
            dir_list = os.listdir(path)
        except WindowsError:
            pass
        for dir_entry in dir_list:
            complete_dir_entry = join(path, dir_entry)
            if isdir(complete_dir_entry):
                dir_queue.append(complete_dir_entry)
            else:
                print(complete_dir_entry)  # print filenames


# path = 'C:\Python27'
# path = 'C:\\'
# list_dir_recursive(path)


dirpath = 'C:\\Users\\vpc\\PycharmProjects'

print('================ recursive dir ================')
list_dir_recursive(dirpath)

print('================ iterative dir ==============')
list_dir_iterative(dirpath)


for dirpath, dirnames, filenames in os.walk(r'c:\\temp'):
    print(dirpath, dirnames, filenames)
    # for dirname in dirnames:
    #     print(dirpath + '\\' + dirname)
    # for filename in filenames:
    #     print(dirpath + '\\' + filename)
