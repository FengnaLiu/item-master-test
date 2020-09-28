import sys
from datetime import datetime, timedelta, timezone

if __name__ == '__main__':

    N = "000000005"
    N_1 = "000000008"

    path = 'item-master-file-generate/sejitem_item_20200929.dat'
    header = "H" + "20200929".ljust(134, " ")
    tailer = "E" + N.ljust(134, " ")

    path_1 = 'item-master-file-generate/sejitem_item_20200928.dat'
    header_1 = "H" + "20200928".ljust(134, " ")
    tailer_1 = "E" + N_1.ljust(134, " ")

    data_list = []

    data_list.append(
        "D" + str(991002).rjust(6, "0") + "20200901" + "99991231" + "00B20022" + (
                "kananame" + str(991002).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991002).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list.append(
        "D" + str(991003).rjust(6, "0") + "20200801" + "99991231" + "00B20022" + (
                "kananame" + str(991003).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991003).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list.append(
        "D" + str(991005).rjust(6, "0") + "20200901" + "99991231" + "00B20022" + (
                "kananame" + str(991005).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991005).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")

    data_list1 = []

    data_list1.append(
        "D" + str(991001).rjust(6, "0") + "20200901" + "99991231" + "00B20022" + (
                "kananame" + str(991001).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991001).rjust(6, "0")).ljust(44,
                                                              " ") + "11001012010980 4901777348479" + "\r\n")
    data_list1.append(
        "D" + str(991001).rjust(6, "0") + "20200801" + "20200831" + "00B20022" + (
                "kananame" + str(991001).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991001).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list1.append(
        "D" + str(991002).rjust(6, "0") + "20200801" + "99991231" + "00B20022" + (
                "kananame" + str(991002).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991002).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list1.append(
        "D" + str(991003).rjust(6, "0") + "20200901" + "99991231" + "00B20022" + (
                "kananame" + str(991003).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991003).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list1.append(
        "D" + str(991004).rjust(6, "0") + "20200901" + "99991231" + "00B20022" + (
                "kananame" + str(991004).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991004).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list1.append(
        "D" + str(991005).rjust(6, "0") + "20200901" + "99991231" + "00B20022" + (
                "kananame" + str(991005).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991005).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")

    ## 当日分のバイナリーファイルの書き込み
    with open(path, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        for i in range(3):
            f.write(data_list[i + 0].encode(encoding='utf-8'))
        f.write(tailer.encode(encoding='utf-8'))

    ## 前日分のバイナリーファイルの書き込み
    with open(path_1, mode='wb') as f:
        f.write(header_1.encode(encoding='utf-8'))
        for i in range(6):
            f.write(data_list1[i + 0].encode(encoding='utf-8'))
        f.write(tailer_1.encode(encoding='utf-8'))
