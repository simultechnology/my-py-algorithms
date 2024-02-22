from os import listdir
from os.path import isfile, join
from collections import deque


def print_names(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir_name = search_queue.popleft()
        for file in sorted(listdir(dir_name)):
            full_path = join(dir_name, file)
            if isfile(full_path):
                print(full_path)
            else:
                search_queue.append(full_path)


def print_name_recursive(start_dir):
    for file in sorted(listdir(start_dir)):
        full_path = join(start_dir, file)
        if isfile(full_path):
            print(full_path)
        else:
            print_name_recursive(full_path)


print_names('../../')
print('-------------------------------------')
print_name_recursive('../../')
