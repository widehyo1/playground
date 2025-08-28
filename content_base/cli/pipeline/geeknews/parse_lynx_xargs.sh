#!/bin/bash
# parse_lynx_xargs.sh

out="bulk_data_lynx.csv"

date
# find sample/ -name '*.html' \
find html/ -name '*.html' \
  | xargs -P "$(nproc)" -I {} bash -c '
      f="{}"
      url="https://news.hada.io/topic?id=$(basename "${f%%.*}")"

      # 필요한 DOM 추출
      parsed=$(htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "$f")

      # 타이틀 추출
      title=$(echo "$parsed" | head -n 1 | awk -F "[<>]" "{ print \$5 }")

      # 본문만 추출 → 텍스트 변환 → CSV escape
      content=$(echo "$parsed" | tail -n +2 | \
        LANG=ko_KR.UTF-8 lynx -stdin -assume_charset=utf-8 -display_charset=utf-8 -dump -nolist -width=1000 | \
        jq -Rs "." | jq -r "[.] | @csv")

      echo "\"$url\",\"$title\",$content"
  ' > "$out"
date
