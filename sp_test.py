import os
import matplotlib

import matplotlib.pyplot as plt
import numpy as np
import scientific_plots as SP
from scientific_plots.default_plots import plot
import pandas

def offset_remove(data):
    average=np.mean(data[0:1000])
    new_data=data - average
    #求出前1000个数的平均值，然后消除offset
    return new_data


def absolute_value(HD_path, data):
    HD_data = pandas.read_table(HD_path, header=None, sep="\t", dtype=str)
    HD_data[1] = HD_data[1].astype("float")
    absolute_data = np.mean(HD_data[1][0:1000])
    print("pressure reference is ", absolute_data)
    data = absolute_data + data
    return data

def find_timing(data):
    for i in range(len(data[1])):
        if data[i] - data[i-1] > 10 * (data[i-1] -data[i-2]):
            return i

if __name__ == '__main__':
    matplotlib.use('TkAgg')
    file_path = "F:\\小论文处理\\Messung T-Stück 04.11.22\\Messung T-Stück 04.11.22\\Druckluftzufuhr zu\\Messung zu\\7 bar\\dls-export-2022-11-04-15-54-57\\p_rel5\\p_rel5.txt"
    #save_path = "F:\\小论文处理\\test\\Druckluftzufuhr zu\\1 bar\\dls-export-2022-11-08-12-00-20\\p_rel1"
    hd_path = "F:\\小论文处理\\Messung T-Stück 04.11.22\\Messung T-Stück 04.11.22\\Druckluftzufuhr zu\\Messung zu\\7 bar\\dls-export-2022-11-04-15-54-57\\p_HD_abs_channel1.dat"
    nd_path = "F:\\小论文处理\\Messung T-Stück 04.11.22\\Messung T-Stück 04.11.22\\Druckluftzufuhr zu\\Messung zu\\7 bar\\dls-export-2022-11-04-15-54-57\\p_ND_abs_channel2.dat"
    my_data = pandas.read_table(file_path, header=None, sep="\t", dtype=str)
    #hd_data = pandas.read_table(hd_path, header=None, sep="\t", dtype=str)
    #print(my_data)

    my_data[0] = my_data[0].astype("float") * 0.000001
    my_data[1] = my_data[1].astype(np.float64)
    # hd_data[0] = hd_data[0].astype("float")
    # hd_data[1] = hd_data[1].astype(np.float64)
    offset_data = offset_remove(my_data[1])
    absdata = absolute_value(nd_path, offset_data) ##############################在这里修改hd 和nd###################

    plt.plot(my_data[0], absdata)
    #plt.plot(my_data[0], offset_data)
    #plt.plot(my_data[0], my_data[1])
    #plt.plot(hd_data[0], hd_data[1])
    plt.xlabel("Time(s)")
    plt.ylabel("RP(MPa)")
    plt.show()
    #plot(my_data[0], my_data[1], "Time(s)", "RP(MPa)", save_path)

