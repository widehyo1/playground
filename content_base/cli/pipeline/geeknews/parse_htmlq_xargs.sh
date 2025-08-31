#!/bin/bash
# bench_xargs.sh
set -euo pipefail
# 설정
# base_dir='split_workspace/sp_1024'
base_dir='split_workspace/sp_128'
selector='span#topic_contents, span.comment_contents'

nproc=${1:-$(nproc)}

# 대상이 되는 모든 서브디렉토리만 가져옴 (파일 제외)
subdirs=$(find "$base_dir" -maxdepth 1 -type d -name "dir_*" | sort)

echo "nproc: $nproc"
# 각 디렉토리에 대해 반복
for dir in $subdirs; do
    echo "[Processing: $dir]"
    outfile="$base_dir/output_${dir##*_}.csv"

    find "$dir" -type f -name "*.html" -printf "%f\n" |
    xargs -P "$nproc" -I {} bash -c '
        f="$1"; dir="$2"
        fullpath="$dir/$f"
        url="https://news.hada.io/topic?id=$(basename "${f%%.*}")"
        title=$(htmlq "div.topictitle.link h1" -t -f "$fullpath")
        content=$(htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "$fullpath" |
            LANG=ko_KR.UTF-8 lynx -assume_charset=utf-8 -display_charset=utf-8 -dump -nolist -width=1000 -stdin |
            jq -Rs "." | jq -r "[.] | @csv")
        echo "\"$url\",\"$title\",$content"
    ' _ {} "$dir" > "$outfile"
done
