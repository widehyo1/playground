#!/bin/bash
f="html/3172.html"

# 전체 시간
echo "[전체 파이프라인]"
time bash -c '
  htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "$0" |
  tail -n +2 |
  pandoc -f html -t markdown |
  jq -Rs "." |
  jq -r "[.] | @csv"
' "$f"

echo
echo "[htmlq]"
time htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents" -f "$f" > /dev/null

echo "[pandoc]"
htmlq "div.topictitle.link a, span#topic_contents, span.comment_contents"  -f "$f" | tail -n +2 > temp.html
time pandoc -f html -t markdown < temp.html > /dev/null

echo "[jq]"
pandoc -f html -t markdown < temp.html > temp.md
time jq -Rs "." < temp.md | jq -r '[.] | @csv' > /dev/null
