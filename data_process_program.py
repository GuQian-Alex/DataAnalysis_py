import os
import matplotlib.pyplot as plt
import numpy as np
import linecache
import scientific_plots as SP
from scientific_plots.default_plots import plot
import pandas
import shutil


def find_txt_length(dir_path):
    """
    寻找文件夹下文件的最小长度
    :param dir_path:
    :return: 返回最下长度
    """
    file_name_list = os.listdir(dir_path)  # 获取文件名
    txt_length_min = np.inf  # 初始化最小长度为无穷大
    for i in file_name_list:  # 遍历文件
        if i == "dls_export_info.txt":
            continue
        file_path = dir_path + "\\" + i  # 合成路径
        with open(file_path, "r") as fp:  # 打开文件
            txt = fp.read().split("\n")  # 读取文件的内容,并分行
            txt_length = len(txt)  # 获取文件的长度
            if txt_length < txt_length_min:
                txt_length_min = txt_length  # 更新最小长度
    return txt_length_min


def cut_txt(dir_path, length):
    """
    根据得到的最小长度，将文件夹下的文件统一为最小长度。裁剪方式：裁剪掉前5：5+m行
    :param dir_path: 文件夹路径
    :param length: 最小文件长度
    :return:
    """
    file_name_list = os.listdir(dir_path)  # 获取文件名
    for i in file_name_list:  # 遍历文件
        file_path = dir_path + "\\" + i  # 合成路径
        fp = open(file_path, "r")  # 打开文件,对文件进行读
        txt = fp.read().split("\n")  # 读取文件的内容,并分行
        fp.close()
        txt_length = len(txt)  # 获取文件长度
        if txt_length > length:  # 如果文件长度大于最小长度，进行裁剪
            cut_line = txt_length - length  # 要裁剪的行数
            txt_1 = txt[0:5]  # 保留的前5行
            txt_2 = txt[5 + cut_line:txt_length]  # 裁剪后剩下的部分
            txt = txt_1 + txt_2  # 合并内容
            fp = open(file_path, "w")  # 打开文件，进行写操作
            # 存储文件
            for i in txt:
                fp.write(str(i) + "\n")
            fp.close()


def my_re_name(dir_path):
    """
    将路径下的文件夹重新命名,并分类
    :param dir_path:
    :return:
    """
    file_name_list = os.listdir(dir_path)  # 读取路径下的文件名
    for i in range(len(file_name_list)):  # 遍历文件名
        file_path = dir_path + "\\" + file_name_list[i]  # 合成文件路径
        text = linecache.getline(file_path, 3)[-9:-1]  # 读取文件中的第4行的倒数9个字符
        new_name = text + "_" + file_name_list[i]  # 根据倒数9个字符重新生成文件名
        new_path = dir_path + "\\" + new_name  # 合成新的文件路径
        os.renames(file_path, new_path)  # rename
        # print(text)


def file_process(dir_path_v, from_line_v, end_line_v, save_path_v, save_file_name):
    """
    :param dir_path_v:
    :param from_line_v:
    :param end_line_v:
    :param save_path_v:
    :param save_file_name:
    :return:
    """
    file_name_list = os.listdir(dir_path_v)  # 获取文件名
    # print(file_name_list)
    file_content_list = []  # 合并后的文件内容  [文件1][...][文件n]
    for i in file_name_list:  # 遍历文件名
        file_path = dir_path_v + "\\" + i  # 合成文件路径
        with open(file_path, "r") as file:  # 打开文件
            temp_content = file.read()  # 读取文件
            file_content_list.append(temp_content)  # 文件内容合并

    for j in range(len(file_content_list)):  # 对合并后的文件进行处理
        file_content_list[j] = file_content_list[j].split("\n")  # 根据文件中的换行符进行分割
        # [[文件1第一行][...][文件1第n行]][...][[文件n第一行][...][文件n第n行]]
    all_list = []
    # num = int(file_content_list[0][from_line_v].split("\t")[0])  # 对第一个文件的指定行进行分割，根据文件中的制表符进行分割，取第一个数据
    num = 0
    while True:

        for p in range(len(file_content_list)):  # 遍历这n个文件
            file_content_list[p][from_line_v] = file_content_list[p][from_line_v].split("\t")  # 对第p个文件从指定行进行分割
            # [[[文件1第一行第一个数据][...][文件1第一行第m个数据]]]
            file_content_list[p][from_line_v][0] = str(num)  # 将指定行的数据替换为num
            num += 50
            file_content_list[p][from_line_v] = file_content_list[p][from_line_v][0] + "\t" + \
                                                    file_content_list[p][from_line_v][1]
            all_list.append(file_content_list[p][from_line_v])  # 将文件的指定行加入到列表中
        from_line_v += 1  # 更换指定行再次进行遍历
        if file_content_list[0][from_line_v] == "":  # 若到达最后一行停止循环
            break

    fp = open(save_path_v + "\\" + save_file_name + ".txt", "w+")  # 将文件写入,并按照指定路径存储
    for i in all_list:
        fp.write(str(i) + "\n")
    fp.close()
    return save_path_v +"\\"+ save_file_name + ".txt"


if __name__ == '__main__':
    # 获取7 bar
    root_path = "F:\\小论文处理\\Messung T-Stück 04.11.22\\Messung T-Stück 04.11.22\\Druckluftzufuhr zu\\Messung zu"
    bar_file_name = os.listdir(root_path)
    for i in range(len(bar_file_name)):
        bar_file_path = root_path + "\\" + bar_file_name[i]
        print("bar_file_path", bar_file_path)
        dls_file_name = os.listdir(bar_file_path)
        for j in range(len(dls_file_name)):
            dls_file_path = bar_file_path + "\\" + dls_file_name[j]
            print("dls_file_path", dls_file_path)
            # 取最短长度
            length_min = find_txt_length(dls_file_path)
            # 裁剪
            cut_txt(dls_file_path, length_min)
            # rename
            my_re_name(dls_file_path)
            # 文件合并
            p_re_name_list = os.listdir(dls_file_path)
            for m in range(len(p_re_name_list)):
                p_re_name_path = dls_file_path + "\\" + p_re_name_list[m]
                if os.path.isdir(p_re_name_path):
                    print("p_re_name_path", p_re_name_path)
                    file_path = file_process(p_re_name_path, 5, length_min, p_re_name_path, p_re_name_list[m])
                    # 画图
                    # my_data = pandas.read_table(file_path, header=None, sep="\t", dtype=str)
                    # my_data[0] = my_data[0].astype("float")
                    # my_data[1] = my_data[1].astype(np.float64)
                    # plt.plot(my_data[0], my_data[1])
                    # plt.show()
                    # plot(my_data[0], my_data[1], "time", "RP", p_re_name_path[m])
            print("_______________________________________________________")
