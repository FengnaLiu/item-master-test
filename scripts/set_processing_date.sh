#!/bin/bash
which gdate >/dev/null 2>&1
if [ $? -eq 0 ]; then
        echo "alias date to gdate." >&2
        shopt -s expand_aliases
        alias date=gdate
fi
PROJECT=$1
TODAY=$(date +'%Y-%m-%d')
YESTERDAY=$(date -d '-1 days' +'%Y-%m-%d')
YESTERDAYCREATEDATE=$(date -d '-2 days' +'%Y-%m-%d')


QueryStr1="UPDATE \`${PROJECT}.dwh.ItemMaster\` SET processing_date='${YESTERDAY}'
WHERE created_date='${YESTERDAYCREATEDATE}' AND item_cd > '900000' "

echo "update processing_date in table: ${PROJECT}.dwh.ItemMaster. Project_id: ${PROJECT}"
echo "Update DML String: ${QueryStr1}."
bq query --project=${PROJECT} --use_legacy_sql=false "${QueryStr1}"

QueryStr2="SELECT processing_date,created_date, item_cd,start_date FROM \`${PROJECT}.dwh.ItemMaster\`
WHERE created_date=DATE('${YESTERDAYCREATEDATE}') AND item_cd > '900000' ORDER BY item_cd"
echo "Check data after updated: ${QueryStr2} "
bq query --project=${PROJECT} --use_legacy_sql=false "${QueryStr2}"
