#!/bin/bash
htmlfile='html/3712.html'
selector='span#topic_contents, span.comment_contents'

htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "$htmlfile" > temp.html
echo "[pandoc]"
pandoc -f html -t markdown < temp.html

echo "[html2text]"
html2text < temp.html

echo "[lynx]"
LANG=ko_KR.UTF-8 lynx -assume_charset=utf-8 -display_charset=utf-8 -dump -nolist -width=1000 temp.html
