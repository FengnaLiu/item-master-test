import sys
from datetime import datetime, timedelta



if __name__ == '__main__':
    env_name="dev"
    today_jst_from_macro="2020-09-18"
    bigquery_insert_sql = "INSERT `seven-central-dwh-{env_name}.dwh.ItemMaster` " \
                          "SELECT created_date, date(\"{today}\") as processing_date, * except(created_date,processing_date) " \
                          "FROM `seven-central-dwh-{env_name}.dwh.ItemMaster` WHERE processing_date = DATE_SUB(\"{today}\", INTERVAL 1 DAY) " \
                          "AND  (item_cd,start_date) not in " \
                          "(select (item_cd,start_date) " \
                          "FROM `seven-central-dwh-dev.dwh.ItemMaster` " \
                          "WHERE processing_date = \"{today}\")".format(env_name=env_name, today=today_jst_from_macro)

    print(bigquery_insert_sql)