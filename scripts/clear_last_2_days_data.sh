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


QueryStr="DELETE \`${PROJECT}.dwh.ItemMaster\` WHERE processing_date in ('${TODAY}','${YESTERDAY}') AND item_cd > '900000'"


echo "Delete data which processing_date is last 2 days in table: ${PROJECT}.dwh.ItemMaster. Project_id: ${PROJECT}"
echo "Query String: ${QueryStr}"
bq query --project=${PROJECT} --use_legacy_sql=false "${QueryStr}"

