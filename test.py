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
    return absolute_data

def find_timing(data):
    for i in range(len(data)):
        if np.absolute(data[i]) > 0.002:
            return i
if __name__ == '__main__':
    matplotlib.use('TkAgg')
    hd_path = "F:\\小论文处理\\test\\Druckluftzufuhr zu\\7 bar\\dls-export-2022-11-08-12-11-32\\p_rel5\\p_rel5.txt"
    #hd_path = "F:\\小论文处理\\test\\Druckluftzufuhr zu\\1 bar\\dls-export-2022-11-08-12-04-54\\p_ND_abs_channel2.dat"
    hd_data = pandas.read_table(hd_path, header=None, sep="\t", dtype=str)
    inject_path = "F:\\小论文处理\\test\\Druckluftzufuhr zu\\7 bar\\dls-export-2022-11-08-12-11-32\\r_signal_channel54.dat"
    in_data = pandas.read_table(inject_path, header=None, sep="\t", dtype=str)
    #hd_data[0] = (hd_data[0].astype("float") -1667903207471051) * 0.000001
    hd_data[0] = hd_data[0].astype("float") * 0.000001
    hd_data[1] = hd_data[1].astype(np.float64)
    in_data[0] = in_data[0].astype("float")
    in_data[1] = in_data[1].astype(np.float64)
    in_data[0] = (in_data[0] - 1667905113953552) * 0.000001
    hd_data[1] = offset_remove(hd_data[1])
    in_data[1] = offset_remove(in_data[1])
    print("injection point number is: ", find_timing(in_data[1]))
    print("p_rel1 point number is: ", find_timing(hd_data[1]))
    print("injection time is: ", find_timing(in_data[1]) * 0.0005)
    print("p_rel1 time is: ", find_timing(hd_data[1]) * 0.00005)
    delta_t = find_timing(hd_data[1]) * 0.00005 - find_timing(in_data[1]) * 0.0005  #####################时间，10倍重采样，需要特别注意！！！！！！！！！！！！####################
    print("time to sensor1 is: ", delta_t)
    print("distant to the 1st sensor is: ", delta_t * 340, "m")


    plt.plot(hd_data[0], hd_data[1])
    plt.plot(in_data[0], in_data[1])
    plt.xlabel("Time(s)")
    plt.ylabel("RP(MPa)")
    plt.show()
