#!/bin/bash
usage() {
  echo "Usage: descendant <TOPIC_ID>" >&2
  exit 1
}

# 인자 파싱
topic_id="$1"

if [[ -z "$topic_id" ]]; then
  usage
fi

title=$(pup 'html > body > main > article > div > div:nth-child(2) > div:nth-child(2) > a > h1 text{}' -f html/$topic_id.html)
href=$(pup 'html > body > main > article > div > div:nth-child(2) > div:nth-child(2) > a attr{href}' -f html/$topic_id.html)
echo "[$title]($href)"
pup 'html > body > main > article > div > div:nth-child(2) > div:nth-child(4) > div > span' -f html/$topic_id.html | pandoc -f html -t markdown
pup 'html > body > main > article > div:nth-child(2)' -f html/$topic_id.html | pandoc -f html -t markdown
