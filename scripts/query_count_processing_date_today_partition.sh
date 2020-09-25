#!/bin/bash
which gdate >/dev/null 2>&1
if [ $? -eq 0 ]; then
        echo "alias date to gdate." >&2
        shopt -s expand_aliases
        alias date=gdate
fi
PROJECT=$1
TODAY=$(date +'%Y-%m-%d')

QueryStr="SELECT count(*) as cnt FROM \`${PROJECT}.dwh.ItemMaster\`
WHERE processing_date='${TODAY}' AND item_cd > '900000' order by item_cd"

echo "Query bigquery table ${PROJECT}.dwh.ItemMaster to count records that processing_date is today. Project_id: ${PROJECT}"
echo "Query String: ${QueryStr} "
bq query --project=${PROJECT} --use_legacy_sql=false "${QueryStr}"

