#!/bin/bash
generate_row() {
    local url="$1"
    local title="$2"
    local md="$3"
    printf "%s\t%s\t%s\n" "$url" "$title" "$md"
}
date
find sample/ -name '*.html' | while read f; do
    url="https://news.hada.io/topic?id=$(basename "${f%%.*}")"
    title=$(pup 'div.topictitle.link h1 text{}' -f "$f")
    md=$(pup 'div.topictitle.link a, span#topic_contents, span.comment_contents' -f "$f" | pandoc -f html -t markdown)
    generate_row "$url" "$title" "$md"
done > bulk_data.tsv
date
