import sys
from datetime import datetime, timedelta, timezone

if __name__ == '__main__':
    today = datetime.now(timezone(timedelta(hours=9))).date()
    today_str = today.strftime("%Y%m%d")
    yesterday = today - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y%m%d")

    start_date_past = today - timedelta(days=200)
    start_date_future = today + timedelta(days=100)
    end_date_past = today - timedelta(days=20)
    end_date_future = today + timedelta(days=300)

    today_file_str = (today - timedelta(days=1)).strftime("%Y%m%d")
    yesterday_file_str = (today - timedelta(days=2)).strftime("%Y%m%d")

    start_date_past_str = start_date_past.strftime("%Y%m%d")
    start_date_future_str = start_date_future.strftime("%Y%m%d")
    end_date_past_str = end_date_past.strftime("%Y%m%d")
    end_date_future_str = end_date_future.strftime("%Y%m%d")

    N = "000000013"
    N_1 = '000000014'

    path_1 = 'item-master-file-generate/pattern1_yesterday.bin'
    path = 'item-master-file-generate/pattern1_today.bin'
    header_1 = "H" + yesterday_file_str.ljust(134, " ")
    header = "H" + today_file_str.ljust(134, " ")
    tailer_1 = "E" + N_1.ljust(134, " ")
    tailer = "E" + N.ljust(134, " ")

    data_list = []
    start_date_list = []
    start_date_list += [start_date_past_str, start_date_past_str, start_date_past_str, today_str, today_str,
                        start_date_future_str]
    end_date_list = []
    end_date_list += [end_date_past_str, today_str, end_date_future_str, end_date_future_str, today_str,
                      end_date_future_str]
    for i in range(6):
        if i == 0:
            for j in range(2):
                data_list.append(
                    "D" + str(j + 1 + 900000).rjust(6, "0") + start_date_list[i] + end_date_list[i] + "00B20022" + (
                            "kananame" + str(j + 1+ 900000).rjust(6, "0")).ljust(30, " ") + (
                            "kanjiname" + str(j + 1+ 900000).rjust(6, "0")).ljust(44,
                                                                          " ") + "11001012010980 4901777348479" + "\r\n")
        else:
            for j in range(3):
                data_list.append(
                    "D" + str(2 + (i - 1) * 3 + j + 1+ 900000).rjust(6, "0") + start_date_list[i] + end_date_list[
                        i] + "00B20022" + (
                            "kananame" + str(2 + (i - 1) * 3 + j + 1+ 900000).rjust(6, "0")).ljust(30, " ") + (
                            "kanjiname" + str(2 + (i - 1) * 3 + j + 1+ 900000).rjust(6, "0")).ljust(44,
                                                                                            " ") + "11001012010980 4901777348479" + "\r\n")

    ## 前日分のバイナリーファイルの書き込み
    with open(path_1, mode='wb') as f:
        f.write(header_1.encode(encoding='utf-8'))
        for j in range(2):
            f.write(data_list[j].encode(encoding='utf-8'))
        for i in range(5):
            f.write(data_list[2 + i * 3 + 0].encode(encoding='utf-8'))
            f.write(data_list[2 + i * 3 + 1].encode(encoding='utf-8'))
        f.write(tailer_1.encode(encoding='utf-8'))

    ## 当日分のバイナリーファイルの書き込み
    with open(path, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        f.write(data_list[0].encode(encoding='utf-8'))
        for i in range(5):
            f.write(data_list[2 + i * 3 + 0].encode(encoding='utf-8'))
            f.write(data_list[2 + i * 3 + 2].encode(encoding='utf-8'))
        f.write(tailer.encode(encoding='utf-8'))
