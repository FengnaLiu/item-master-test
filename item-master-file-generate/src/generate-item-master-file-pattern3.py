import sys
from datetime import datetime, timedelta, timezone

if __name__ == '__main__':
    today = datetime.now(timezone(timedelta(hours=9))).date()
    today_str = today.strftime("%Y%m%d")
    today_file_str = (today - timedelta(days=1)).strftime("%Y%m%d")
    yesterday_file_str = (today - timedelta(days=2)).strftime("%Y%m%d")

    start_date = today - timedelta(days=200)

    end_date = start_date + timedelta(days=300)

    start_date_str = start_date.strftime("%Y%m%d")
    end_date_str = end_date.strftime("%Y%m%d")


    N = "000100002"

    path = 'item-master-file-generate/pattern3_yesterday.bin'
    header = "H" + today_file_str.ljust(134, " ")
    tailer = "E" + N.ljust(134, " ")

    path_1 = 'item-master-file-generate/pattern3_2_days_before.bin'
    header_1 = "H" + yesterday_file_str.ljust(134, " ")
    tailer_1 = "E" + N.ljust(134, " ")

    data_list = []
    for i in range(100000):
        data_list.append(
            "D" + str(i + 1+ 700000).rjust(6, "0") + start_date_str + end_date_str + "00B20022" + (
                    "kananame" + str(i + 1+ 700000).rjust(6, "0")).ljust(30, " ") + (
                    "kanjiname" + str(i + 1+ 700000).rjust(6, "0")).ljust(44,
                                                                  " ") + "11001012010980 4901777348479" + "\r\n")
    data_list1 = []
    for i in range(100000):
        data_list1.append(
            "D" + str(i + 1 + 800000).rjust(6, "0") + start_date_str + end_date_str + "00B20022" + (
                    "kananame" + str(i + 1 + 800000).rjust(6, "0")).ljust(30, " ") + (
                    "kanjiname" + str(i + 1 + 800000).rjust(6, "0")).ljust(44,
                                                                           " ") + "11001012010980 4901777348479" + "\r\n")

    ## 前日分のバイナリーファイルの書き込み
    with open(path, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        for i in range(100000):
            f.write(data_list[i + 0].encode(encoding='utf-8'))
        f.write(tailer.encode(encoding='utf-8'))

    ## 前々日分のバイナリーファイルの書き込み
    with open(path_1, mode='wb') as f:
        f.write(header_1.encode(encoding='utf-8'))
        for i in range(100000):
            f.write(data_list1[i + 0].encode(encoding='utf-8'))
        f.write(tailer_1.encode(encoding='utf-8'))
