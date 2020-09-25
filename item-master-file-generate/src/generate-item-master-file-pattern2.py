import sys
from datetime import datetime, timedelta,timezone


def getStartDate(i, today, duration, start_date_2_end_date_1_diff):
    if i == 1:
        return today + timedelta(days=10)
    elif i == 2:
        return today
    elif i == 3:
        return today - timedelta(days=10)
    elif i == 4:
        return today - timedelta(days=duration)
    elif i == 5:
        return today - timedelta(days=(5 + duration))
    elif i == 6:
        return today - timedelta(days=duration + start_date_2_end_date_1_diff)
    elif i == 7:
        return today - timedelta(days=20 + duration + start_date_2_end_date_1_diff)
    elif i == 8:
        return today - timedelta(days=duration + start_date_2_end_date_1_diff + duration)
    elif i == 9:
        return today - timedelta(20 + duration + start_date_2_end_date_1_diff + duration)



if __name__ == '__main__':
    today = datetime.now(timezone(timedelta(hours=9))).date()
    today_str = today.strftime("%Y%m%d")
    duration = 100
    start_date_2_end_date_1_diff = 10
    one_day_before = today - timedelta(days=1)
    one_day_before_str = one_day_before.strftime("%Y%m%d")

    N = "000000038"
    N_1 = '000000074'

    path_1 = 'pattern2_one_day_before.bin'
    path = 'patttern2_today.bin'
    header_1 = "H" + one_day_before_str.ljust(134, " ")
    header = "H" + today_str.ljust(134, " ")
    tailer_1 = "E" + N_1.ljust(134, " ")
    tailer = "E" + N.ljust(134, " ")

    data_list = []
    for i in range(9):
        start_date_1 = getStartDate(i + 1, today, duration, start_date_2_end_date_1_diff)
        end_date_1 = start_date_1 + timedelta(days=duration)
        start_date_2 = end_date_1 + timedelta(days=start_date_2_end_date_1_diff)
        end_date_2 = start_date_2 + timedelta(days=duration)
        for j in range(4):
            data_list.append(
                "D9" + str(i * 4 + j + 1).rjust(5, "0") + start_date_1.strftime("%Y%m%d") + end_date_1.strftime(
                    "%Y%m%d") + "00B20022" + (
                        "kananame9" + str(i * 4 + j + 1).rjust(5, "0")).ljust(30, " ") + (
                        "kanjiname9" + str(i * 4 + j + 1).rjust(5, "0")).ljust(44,
                                                                               " ") + "11001012010980 4901777348479" + "\r\n")
            data_list.append(
                "D9" + str(i * 4 + j + 1).rjust(5, "0") + start_date_2.strftime("%Y%m%d") + end_date_2.strftime(
                    "%Y%m%d") + "00B20022" + (
                        "kananame9" + str(i * 4 + j + 1).rjust(5, "0")).ljust(30, " ") + (
                        "kanjiname9" + str(i * 4 + j + 1).rjust(5, "0")).ljust(44,
                                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    print(data_list)

    ## 当日分のバイナリーファイルの書き込み
    with open(path, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        for i in range(9):
            f.write(data_list[i * 8 + 0].encode(encoding='utf-8'))
            f.write(data_list[i * 8 + 1].encode(encoding='utf-8'))
            f.write(data_list[i * 8 + 2].encode(encoding='utf-8'))
            f.write(data_list[i * 8 + 5].encode(encoding='utf-8'))

        f.write(tailer.encode(encoding='utf-8'))

    ## 前日分のバイナリーファイルの書き込み
    with open(path_1, mode='wb') as f:
        f.write(header_1.encode(encoding='utf-8'))
        for i in range(len(data_list)):
            f.write(data_list[i].encode(encoding='utf-8'))
        f.write(tailer_1.encode(encoding='utf-8'))
