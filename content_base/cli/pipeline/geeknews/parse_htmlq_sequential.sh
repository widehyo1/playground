#!/bin/bash
# bench_xargs.sh
set -euo pipefail
# 설정
base_dir='html'
selector='span#topic_contents, span.comment_contents'
outfile="bulk_data_seq.csv"

find "$base_dir" -type f -name "*.html" -printf "%f\n" | sort -n |
while IFS= read -r f; do
    fullpath="$base_dir/$f"
    url="https://news.hada.io/topic?id=$(basename "${f%%.*}")"
    title=$(htmlq "div.topictitle.link h1" -t -f "$fullpath")
    content=$(htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "$fullpath" |
        LANG=ko_KR.UTF-8 lynx -assume_charset=utf-8 -display_charset=utf-8 -dump -nolist -width=1000 -stdin |
        jq -Rs "." | jq -r "[.] | @csv")
    echo "\"$url\",\"$title\",$content"
done > "$outfile"
