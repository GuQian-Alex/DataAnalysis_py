import os
import linecache


def my_re_name(dir_path):
    file_name_list = os.listdir(dir_path)
    for i in range(len(file_name_list)):
        file_path = dir_path + "\\" + file_name_list[i]
        text = linecache.getline(file_path, 3)[-9:-1]
        new_name = text + "_" + file_name_list[i]
        new_path = dir_path + "\\" + new_name
        os.renames(file_path, new_path)
        print(text)


if __name__ == '__main__':
    dir_path = "F:\\小论文处理\\L\\L_1\\l_1_1"
    my_re_name(dir_path)
