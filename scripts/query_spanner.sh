#!/bin/bash
which gdate >/dev/null 2>&1
if [ $? -eq 0 ]; then
        echo "alias date to gdate." >&2
        shopt -s expand_aliases
        alias date=gdate
fi
PROJECT=$1
TODAY=$(date +'%Y-%m-%d')

QueryStr="SELECT created_date, item_cd, start_date,end_date,sales_status FROM ItemMaster WHERE item_cd > '900000'"

echo "Query spanner table to list records.
Project_id: ${PROJECT}, Dataset: store-items, Instance: seven-central-dwh, Table: ItemMaster."

echo "Query String: ${QueryStr}"
gcloud spanner databases execute-sql  store-items --instance=seven-central-dwh --project=${PROJECT} --sql="${QueryStr}"
