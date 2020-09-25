#!/bin/bash
which gdate >/dev/null 2>&1
if [ $? -eq 0 ]; then
        echo "alias date to gdate." >&2
        shopt -s expand_aliases
        alias date=gdate
fi
PROJECT=$1


QueryStr="DELETE ItemMaster WHERE item_cd > '900000'"

echo "Clear in spanner table. Project_id: ${PROJECT}, Instance: seven-central-dwh, Dataset: store-items, Table: ItemMaster."
echo "Query String: ${QueryStr}"

gcloud spanner databases execute-sql  store-items --instance=seven-central-dwh --project=${PROJECT} --sql="${QueryStr}" --enable-partitioned-dml
