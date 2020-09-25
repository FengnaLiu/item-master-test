#!/bin/bash
which gdate >/dev/null 2>&1
if [ $? -eq 0 ]; then
        echo "alias date to gdate." >&2
        shopt -s expand_aliases
        alias date=gdate
fi
PROJECT=$1
TODAY=$(date +'%Y-%m-%d')

QueryStr="SELECT processing_date, created_date, item_cd, start_date,end_date FROM \`${PROJECT}.dwh.ItemMaster\`
WHERE processing_date=DATE('${TODAY}')
AND created_date IN (DATE_SUB('${TODAY}', INTERVAL 2 DAY)) AND item_cd > '900000' order by item_cd"

echo "Query bigquery table ${PROJECT}.dwh.ItemMaster to search difference between yesterday and today partition. Project_id: ${PROJECT}"
echo "Query String: ${QueryStr} "
bq query --project=${PROJECT} --use_legacy_sql=false "${QueryStr}"

