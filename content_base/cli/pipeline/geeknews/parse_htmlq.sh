#!/bin/bash
generate_row() {
    local url="$1"
    local title="$2"
    local md="$3"
    printf "%s\t%s\t%s\n" "$url" "$title" "$md"
}
date
find html/ -name '*.html' | while read f; do
    url="https://news.hada.io/topic?id=$(basename "${f%%.*}")"
    title=$(htmlq 'div.topictitle.link h1' -t -f "$f")
    md=$(htmlq 'div.topictitle.link a, span#topic_contents, span.comment_contents' -f "$f" | pandoc -f html -t markdown)
    generate_row "$url" "$title" "$md"
done > bulk_data.tsv
date
