import os
import matplotlib.pyplot as plt
import numpy as np


def file_process(dir_path_v, from_line_v, end_line_v, save_path_v):
    file_name_list = os.listdir(dir_path_v)
    print(file_name_list)
    file_content_list = []
    for i in file_name_list:
        file_path = dir_path_v + "\\" + i
        with open(file_path, "r") as file:
            temp_content = file.read()
            file_content_list.append(temp_content)

    for j in range(len(file_content_list)):
        file_content_list[j] = file_content_list[j].split("\n")
    all_list = []
    num = int(file_content_list[0][from_line_v].split("\t")[0])
    while True:
        for p in range(len(file_content_list)):
            file_content_list[p][from_line_v] = file_content_list[p][from_line_v].split("\t")
            file_content_list[p][from_line_v][0] = str(num)
            num += 50
            file_content_list[p][from_line_v] = file_content_list[p][from_line_v][0] + "\t" + \
                                                file_content_list[p][from_line_v][1]
            all_list.append(file_content_list[p][from_line_v])
        from_line_v += 1
        if from_line_v == end_line_v:
            break

    fp = open(save_path_v + "all_content.txt", "w+")
    for i in all_list:
        fp.write(str(i) + "\n")
    fp.close()
    return save_path_v + "all_content.txt"


if __name__ == '__main__':
    dir_path = "F:\\小论文处理\\L\\L_1\\l_1_1\\p_rel5"
    from_line = 5
    end_line = 2805
    save_path = "F:\\小论文处理\\L\\L_1\\l_1_1\\p_rel5\\"
    file_path = file_process(dir_path, from_line, end_line, save_path)

