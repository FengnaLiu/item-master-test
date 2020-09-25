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

QueryStr1="UPDATE ItemMaster
SET start_date=DATE_SUB('${TODAY}', INTERVAL ${n}*2 DAY), end_date=DATE_SUB('${TODAY}', INTERVAL ${n} DAY), sales_status='0'
WHERE item_cd > '900000' "

echo "Set start_date,end_date and sales_status for table ItemMaster. Project_id: ${PROJECT}"
echo "Update DML String: ${QueryStr1} "
gcloud spanner databases execute-sql  store-items --instance=seven-central-dwh --project=${PROJECT} --sql="${QueryStr1}"


QueryStr2="SELECT created_date,item_cd,start_date, end_date, sales_status FROM ItemMaster
WHERE item_cd > '900000' ORDER BY item_cd"
echo "Check data after updated: ${QueryStr2} "
gcloud spanner databases execute-sql  store-items --instance=seven-central-dwh --project=${PROJECT} --sql="${QueryStr2}"


