#!/bin/bash
which gdate >/dev/null 2>&1
if [ $? -eq 0 ]; then
        echo "alias date to gdate." >&2
        shopt -s expand_aliases
        alias date=gdate
fi
PROJECT=$1
TODAY=$(date +'%Y-%m-%d')

n=184

QueryStr1="UPDATE \`${PROJECT}.dwh.ItemMaster\`
SET start_date=DATE_SUB('${TODAY}', INTERVAL ${n}*2 DAY),
end_date=DATE_SUB('${TODAY}', INTERVAL ${n} DAY),
sales_status='0'
WHERE processing_date=DATE('${TODAY}') AND item_cd > '900000'"

echo "Set start_date, end_date and sales_status for table ${PROJECT}.dwh.ItemMaster. Project_id: ${PROJECT}"
echo "Update DML String: ${QueryStr1} "
bq query --project=${PROJECT} --use_legacy_sql=false "${QueryStr1}"

QueryStr2="SELECT processing_date,item_cd,start_date, end_date, sales_status FROM \`${PROJECT}.dwh.ItemMaster\`
WHERE processing_date=DATE('${TODAY}') ORDER BY item_cd"
echo "Check data after updated: ${QueryStr2} "
bq query --project=${PROJECT} --use_legacy_sql=false "${QueryStr2}"
