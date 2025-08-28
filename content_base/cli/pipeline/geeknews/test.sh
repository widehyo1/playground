#!/bin/bash
# htmlq로 content만 추출
htmlq 'span#topic_contents, span.comment_contents' -f html/3172.html > temp.html

echo "[pandoc]"
# pandoc
time pandoc -f html -t markdown < temp.html > /dev/null

echo "[html2text]"
# html2text
time html2text < temp.html > /dev/null

echo "[lynx]"
# lynx
time LANG=ko_KR.UTF-8 lynx -assume_charset=utf-8 -display_charset=utf-8 -dump -nolist -width=1000 temp.html > /dev/null
