#!/bin/bash
# bench_xargs.sh

out="bulk_data_xargs_v2.csv"

date
# find sample/ -name '*.html' \
# find html/ -name '*.html' \
find split_workspace/sp_128/dir_sp_128_00 -name '*.html' \
  | xargs -P "$(nproc)" -I {} bash -c '
      f="{}"
      url="https://news.hada.io/topic?id=$(basename "${f%%.*}")"
      parsed=$(htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "$f")
      title=$(echo "$parsed" | head -n 1 | awk -F "[<>]" "{ print \$5 }")
      md=$(echo "$parsed" | tail -n +2 | pandoc -f html -t markdown | jq -Rs "." | jq -r "[.] | @csv")
      echo "\"$url\",\"$title\",$md"
  ' > "$out"
date
