#!/bin/bash
which gdate >/dev/null 2>&1
if [ $? -eq 0 ]; then
        echo "alias date to gdate." >&2
        shopt -s expand_aliases
        alias date=gdate
fi
PROJECT=$1
TODAY=$(date +'%Y-%m-%d')

QueryStr="SELECT processing_date,created_date,item_cd, start_date,end_date, sales_status FROM \`${PROJECT}.dwh.ItemMaster\`
WHERE processing_date='${TODAY}' AND start_date <= '${TODAY}' AND end_date <= DATE_SUB('${TODAY}', INTERVAL 183 DAY) AND item_cd > '900000'"

echo "Query String: ${QueryStr} "
bq query --project=${PROJECT} --use_legacy_sql=false "${QueryStr}"

