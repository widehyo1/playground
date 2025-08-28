#!/bin/bash
# bench_xargs.sh

out="bulk_data_xargs.tsv"

date
find html/ -name '*.html' \
  | xargs -P "$(nproc)" -I {} bash -c '
      f="{}"
      url="https://news.hada.io/topic?id=$(basename "${f%%.*}")"
      title=$(htmlq "div.topictitle.link h1" -t -f "$f")
      md=$(htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "$f" \
           | pandoc -f html -t markdown)
      printf "%s\t%s\t%s\n" "$url" "$title" "$md"
  ' > "$out"
date
