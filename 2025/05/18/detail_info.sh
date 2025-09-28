#!/bin/bash

arr=(
"009240"
# "038390"
# "334890"
)

for value in "${arr[@]}"; do
    echo curl -q https://finance.naver.com/item/coinfo.naver?code=$value | iconv -c --from-code=EUC-KR --to-code=UTF-8
    curl -q https://finance.naver.com/item/coinfo.naver?code=$value | iconv -c --from-code=EUC-KR --to-code=UTF-8
done

