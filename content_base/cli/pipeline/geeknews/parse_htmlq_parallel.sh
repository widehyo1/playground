#!/bin/bash
# bench_parallel.sh

out="bulk_data_parallel.csv"

date
# find html/ -name '*.html' | parallel -j$(nproc) '
find split_workspace/sp_128/dir_sp_128_00/ -name '*.html' | parallel -j$(nproc) '
  f={};
  url="https://news.hada.io/topic?id=$(basename "${f%%.*}")";
  title=$(htmlq "div.topictitle.link h1" -t -f "$f");
  md=$(htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "$f" \
       | pandoc -f html -t markdown);
  printf "%s\t%s\t%s\n" "$url" "$title" "$md"
' > "$out"
date
