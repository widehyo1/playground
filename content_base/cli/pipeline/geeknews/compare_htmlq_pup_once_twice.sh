#!/bin/bash
test_file="html/3712.html"  # 테스트할 파일 하나만 선택
basename_id=$(basename "${test_file%%.*}")

measure_time_ms() {
    local cmd="$1"
    local start end elapsed
    start=$(date +%s%3N)  # milliseconds
    eval "$cmd"
    end=$(date +%s%3N)
    elapsed=$((end - start))
    echo "$elapsed"
}

echo ""
echo "[htmlq]"
echo ""

echo "▶ Measuring htmlq_once pipeline..."
measure_time_ms '
parsed=$(htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "'"$test_file"'")
' && echo "htmlq_once: htmlq parse 완료"

measure_time_ms '
title=$(echo "$parsed" | head -n 1 | awk -F "[<>]" "{ print \$5 }")
' && echo "htmlq_once: title 추출 완료"

measure_time_ms '
md=$(echo "$parsed" | tail -n +2 | LANG=ko_KR.UTF-8 lynx -assume_charset=utf-8 -display_charset=utf-8 -dump -nolist -width=1000 -stdin | jq -Rs "." | jq -r "[.] | @csv")
' && echo "htmlq_once: lynx + jq 완료"

echo ""
echo "▶ Measuring htmpq_twice pipeline..."

measure_time_ms '
title=$(htmlq "div.topictitle.link h1" -t -f "'"$test_file"'")
' && echo "htmpq_twice: title 추출 완료"

measure_time_ms '
md=$(htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "'"$test_file"'" | LANG=ko_KR.UTF-8 lynx -assume_charset=utf-8 -display_charset=utf-8 -dump -nolist -width=1000 -stdin | jq -Rs "." | jq -r "[.] | @csv")
' && echo "htmpq_twice: 본문 추출 완료"

#################
echo ""
echo "[pup]"
echo ""

echo "▶ Measuring pup_once pipeline..."
measure_time_ms '
parsed=$(pup "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "'"$test_file"'")
' && echo "pup_once: pup parse 완료"

measure_time_ms '
title=$(echo "$parsed" | head -n 1 | awk -F "[<>]" "{ print \$5 }")
' && echo "pup_once: title 추출 완료"

measure_time_ms '
md=$(echo "$parsed" | tail -n +2 | LANG=ko_KR.UTF-8 lynx -assume_charset=utf-8 -display_charset=utf-8 -dump -nolist -width=1000 -stdin | jq -Rs "." | jq -r "[.] | @csv")
' && echo "pup_once: lynx + jq 완료"

echo ""
echo "▶ Measuring pup_twice pipeline..."

measure_time_ms '
title=$(pup "div.topictitle.link h1 text{}" -f "'"$test_file"'")
' && echo "pup_twice: title 추출 완료"

measure_time_ms '
md=$(pup "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "'"$test_file"'" | LANG=ko_KR.UTF-8 lynx -assume_charset=utf-8 -display_charset=utf-8 -dump -nolist -width=1000 -stdin | jq -Rs "." | jq -r "[.] | @csv")
' && echo "pup_twice: 본문 추출 완료"
