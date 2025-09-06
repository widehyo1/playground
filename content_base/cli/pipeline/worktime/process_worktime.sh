#!/bin/bash
echo "making worktime_collect.http"
awk -f ./gen_http.awk date.txt > worktime_collect.http
httpyac worktime_collect.http --all | awk -f ./extract_content.awk | jq -s '.' | jq -rf ./convert_csv.jq | csvcut -c date,pjtNm,workTitle | csvsort -c date,pjtNm > worktime_processed2.csv
echo "worktime_processed2.csv done"
