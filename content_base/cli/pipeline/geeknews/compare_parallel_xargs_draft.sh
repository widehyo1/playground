#!/bin/bash
# profile html parse
set -euo pipefail
# target_dir='split_workspace/sp_1024/dir_html_00'
target_dir='split_workspace/sp_128/dir_sp_128_00'
selector='span#topic_contents, span.comment_contents'

outfile="bulk_data.csv"
out_parallel="bulk_parallel.csv"
out_xargs="bulk_xargs.csv"

measure_time_ms() {
    local cmd="$1"
    local start end elapsed
    start=$(date +%s%3N)  # milliseconds
    eval "$cmd"
    end=$(date +%s%3N)
    elapsed=$((end - start))
    echo "$elapsed"
}

run_profiling() {
    local target_dir="$1"
    local start end elapsed

    echo "flag1"

    start=$(date +%s%3N)  # milliseconds
    find "$target_dir" -type f -name "*.html" -printf "%f\n" | sort -n | while IFS= read -r f; do
        local fullpath="$target_dir/$f"
        local url title content
        url="https://news.hada.io/topic?id=$(basename "${f%%.*}")"
        title=$(htmlq "div.topictitle.link h1" -t -f "$fullpath")
        content=$(htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "$fullpath" | LANG=ko_KR.UTF-8 lynx -assume_charset=utf-8 -display_charset=utf-8 -dump -nolist -width=1000 -stdin | jq -Rs "." | jq -r "[.] | @csv")
        echo "\"$url\",\"$title\",$content"
    done > "$outfile"
    end=$(date +%s%3N)
    elapsed=$((end - start))

    echo "single execution elapsed: $elapsed"

    echo "flag2"
    start=$(date +%s%3N)  # milliseconds
    find "$target_dir" -type f -name "*.html" -printf "%f\n" \
      | xargs -P "$(nproc)" -I {} bash -c '
          f="{}"
          target_dir="$2"
          fullpath="$target_dir/$f"
          url="https://news.hada.io/topic?id=$(basename "${f%%.*}")"
          title=$(htmlq "div.topictitle.link h1" -t -f "$fullpath")
          content=$(htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "$fullpath" | LANG=ko_KR.UTF-8 lynx -assume_charset=utf-8 -display_charset=utf-8 -dump -nolist -width=1000 -stdin | jq -Rs "." | jq -r "[.] | @csv")
          echo "\"$url\",\"$title\",$content"
      ' _ "{}" "$target_dir" > "$out_xargs"
    end=$(date +%s%3N)
    elapsed=$((end - start))

    echo "xargs execution elapsed: $elapsed"

    echo "flag3"
    start=$(date +%s%3N)  # milliseconds

    export target_dir  # export 해야 --env에서 참조 가능

    find "$target_dir" -type f -name "*.html" -printf "%f\n" \
      | parallel --env target_dir -j$(nproc) '
          f="{}"
          fullpath="$target_dir/$f"
          url="https://news.hada.io/topic?id=$(basename "${f%%.*}")"
          title=$(htmlq "div.topictitle.link h1" -t -f "$fullpath")
          content=$(htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "$fullpath" | LANG=ko_KR.UTF-8 lynx -assume_charset=utf-8 -display_charset=utf-8 -dump -nolist -width=1000 -stdin | jq -Rs "." | jq -r "[.] | @csv")
          echo "\"$url\",\"$title\",$content"
      ' > "$out_parallel"
    end=$(date +%s%3N)
    elapsed=$((end - start))

    echo "parallel execution elapsed: $elapsed"
}

# Run both tools
run_profiling "$target_dir"
