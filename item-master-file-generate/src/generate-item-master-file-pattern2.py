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

    yesterday_file_str = (today - timedelta(days=1)).strftime("%Y%m%d")
    today_file_str = (today).strftime("%Y%m%d")
    tomorrow_file_str = (today + timedelta(days=1)).strftime("%Y%m%d")

    start_date_past_str = start_date_past.strftime("%Y%m%d")
    start_date_future_str = start_date_future.strftime("%Y%m%d")
    end_date_past_str = end_date_past.strftime("%Y%m%d")
    end_date_future_str = end_date_future.strftime("%Y%m%d")

    N_0 = "000000014"
    N_1= "000000019"
    N_2 = "000000005"

    path_0 = 'item-master-file-generate/pattern2_yesterday.bin'
    path_1 = 'item-master-file-generate/pattern2_today.bin'
    path_2 = 'item-master-file-generate/pattern2_tomorrow.bin'
    header_0 = "H" + yesterday_file_str.ljust(134, " ")
    header_1 = "H" + today_file_str.ljust(134, " ")
    header_2 = "H" + tomorrow_file_str.ljust(134, " ")
    tailer_0 = "E" + N_0.ljust(134, " ")
    tailer_1 = "E" + N_1.ljust(134, " ")
    tailer_2 = "E" + N_2.ljust(134, " ")

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
                            "kananame" + str(j + 1 + 900000).rjust(6, "0")).ljust(30, " ") + (
                            "kanjiname" + str(j + 1 + 900000).rjust(6, "0")).ljust(44,
                                                                                   " ") + "11001012010980 4901777348479" + "\r\n")
        else:
            for j in range(3):
                data_list.append(
                    "D" + str(2 + (i - 1) * 3 + j + 1 + 900000).rjust(6, "0") + start_date_list[i] + end_date_list[
                        i] + "00B20022" + (
                            "kananame" + str(2 + (i - 1) * 3 + j + 1 + 900000).rjust(6, "0")).ljust(30, " ") + (
                            "kanjiname" + str(2 + (i - 1) * 3 + j + 1 + 900000).rjust(6, "0")).ljust(44,
                                                                                                     " ") + "11001012010980 4901777348479" + "\r\n")

    data_list_api_today = []
    data_list_api_today.append(
        "D" + str(991001).rjust(6, "0") + "20200901" + "99999999" + "00C20022" + (
                "kananame" + str(991001).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991001).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list_api_today.append(
        "D" + str(991001).rjust(6, "0") + "20200801" + "20200831" + "00B20022" + (
                "kananame" + str(991001).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991001).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list_api_today.append(
        "D" + str(991002).rjust(6, "0") + "20200801" + "99999999" + "00B20022" + (
                "kananame" + str(991002).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991002).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list_api_today.append(
        "D" + str(991003).rjust(6, "0") + "20200901" + "99999999" + "00B20022" + (
                "kananame" + str(991003).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991003).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list_api_today.append(
        "D" + str(991004).rjust(6, "0") + "20200901" + "99999999" + "00B20022" + (
                "kananame" + str(991004).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991004).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list_api_today.append(
        "D" + str(991005).rjust(6, "0") + "20200901" + "99999999" + "00B20022" + (
                "kananame" + str(991005).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991005).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")

    data_list_api_tomorrow = []
    data_list_api_tomorrow.append(
        "D" + str(991002).rjust(6, "0") + "20200901" + "99999999" + "00C20022" + (
                "kananame" + str(991002).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991002).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list_api_tomorrow.append(
        "D" + str(991003).rjust(6, "0") + "20200801" + "99999999" + "00C20022" + (
                "kananame" + str(991003).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991003).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")
    data_list_api_tomorrow.append(
        "D" + str(991005).rjust(6, "0") + "20200901" + "99999999" + "00B20022" + (
                "kananame" + str(991005).rjust(6, "0")).ljust(30, " ") + (
                "kanjiname" + str(991005).rjust(6, "0")).ljust(44,
                                                               " ") + "11001012010980 4901777348479" + "\r\n")

    ## 前日分のバイナリーファイルの書き込み
    with open(path_0, mode='wb') as f:
        f.write(header_0.encode(encoding='utf-8'))
        for j in range(2):
            f.write(data_list[j].encode(encoding='utf-8'))
        for i in range(5):
            f.write(data_list[2 + i * 3 + 0].encode(encoding='utf-8'))
            f.write(data_list[2 + i * 3 + 1].encode(encoding='utf-8'))
        f.write(tailer_0.encode(encoding='utf-8'))

    ## 当日分のバイナリーファイルの書き込み
    with open(path_1, mode='wb') as f:
        f.write(header_1.encode(encoding='utf-8'))
        f.write(data_list[0].encode(encoding='utf-8'))
        for i in range(5):
            f.write(data_list[2 + i * 3 + 0].encode(encoding='utf-8'))
            f.write(data_list[2 + i * 3 + 2].encode(encoding='utf-8'))
        for i in range(6):
            f.write(data_list_api_today[i + 0].encode(encoding='utf-8'))
        f.write(tailer_1.encode(encoding='utf-8'))

    ## 明日分のバイナリーファイルの書き込み
    with open(path_2, mode='wb') as f:
        f.write(header_2.encode(encoding='utf-8'))
        for i in range(3):
            f.write(data_list_api_tomorrow[i + 0].encode(encoding='utf-8'))
        f.write(tailer_2.encode(encoding='utf-8'))
