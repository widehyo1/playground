```bash
# script2.awk
BEGIN {
    FS = "/"
    OFS = ":"
}
{
    "yes 'field1 field2 field3 field4 field5 field6'" | getline format
    # occurence_count = split(format, format_arr, " ")
    split(format, format_arr, " ")
    format_arr[3] = $3
    format_arr[6] = $NF
    acc = NR ":"
    for (idx in format_arr) {
        cur = format_arr[idx]
        acc = acc "|" cur
    }
    print acc
}

# script.awk
BEGIN {
    FS = "/"
    OFS = ":"
}
{
    "yes 'field1 field2 field3 field4 field5 field6'" | getline format
    # occurence_count = split(format, format_arr, " ")
    split(format, format_arr, " ")
    # format_arr = split(format, " ") for python user
    acc = NR ":"
    for (idx in format_arr) {
        #cur = idx == 1? $1 : format_arr[idx]
        #cur = idx == 2? $2 : format_arr[idx]
        cur = idx == 3? $3 : format_arr[idx]
        #cur = idx == 4? $4 : format_arr[idx]
        cur = idx == 6? $NF : format_arr[idx]
        acc = acc "|" cur
    }
    print acc
}

---

# temp.txt
api_service/api_service/app/common/util/execution_tree_util.py
api_service/api_service/app/common/util/report_util.py
api_service/api_service/app/post_processor/manage_report_records.py
api_service/api_service/app/post_processor/mapper/fetch.py
api_service/api_service/app/post_processor/processor/gumi/food_festival/consumption_analysis.py
api_service/api_service/app/post_processor/processor/gumi/food_festival/sns_anlysis.py
api_service/api_service/app/post_processor/processor/gumi/food_festival/vpop_analysis.py
api_service/api_service/app/post_processor/vo/report_info.py


# console output
ai_agent on  dev-api [?⇡] ❯ !!
awk -f script2.awk temp.txt
1:|field1|field2|app|field4|field5|execution_tree_util.py
2:|field1|field2|app|field4|field5|report_util.py
3:|field1|field2|app|field4|field5|manage_report_records.py
4:|field1|field2|app|field4|field5|fetch.py
5:|field1|field2|app|field4|field5|consumption_analysis.py
6:|field1|field2|app|field4|field5|sns_anlysis.py
7:|field1|field2|app|field4|field5|vpop_analysis.py
8:|field1|field2|app|field4|field5|report_info.py
9:|field1|field2||field4|field5|
```
