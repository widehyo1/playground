#!/usr/bin/env bash
# dir2dot.sh  ──  사용법:  ./dir2dot.sh /path/to/dir > tree.dot
root="${1%/}"            # 끝 슬래시 제거
echo 'digraph G {'
echo '  graph  [rankdir=LR, splines=ortho, nodesep=0.25]'
echo '  node   [fontname="monospace", fontsize=11]'
echo '  edge   [arrowhead=none]'

# find: -printf '%P|%y\n'  ⇒  상대경로|타입(d=dir,f=file,…)
find "$root" -printf '%P|%y\n' |
while IFS='|' read -r relpath typ; do
  # 첫 줄은 빈 경로(=root)일 수 있으므로 건너뜀
  [[ -z "$relpath" ]] && continue

  abs="\"$root/$relpath\""
  base="$(basename "$relpath")"
  parent="$(dirname  "$relpath")"
  [[ "$parent" == "." ]] && parent=""

  # 노드 자체를 먼저 정의 (모양은 폴더/파일 구분)
  if [[ $typ == d ]]; then
    echo "  $abs [label=\"$base\", shape=folder]"
  else
    echo "  $abs [label=\"$base\", shape=note]"
  fi

  # 부모→자식 간선
  if [[ -n "$parent" ]]; then
    echo "  \"$root/$parent\" -> $abs"
  fi
done

echo '}'
