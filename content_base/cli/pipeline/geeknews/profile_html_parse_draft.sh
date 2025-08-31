#!/bin/bash
# html pipe profile
set -euo pipefail
target_dir='split_workspace/sp_128/dir_sp_128_00'
selector='span#topic_contents, span.comment_contents'

profile_pup() {
    local htmlfile="$1"
    local selector="$2"
    time pup "$selector" < "$htmlfile" > /dev/null
}

profile_htmlq() {
    local htmlfile="$1"
    local selector="$2"
    time htmlq "$selector" < "$htmlfile" > /dev/null
}

echo "[pup]"
find "$target_dir" -type f -name "*.html" -printf "%f\n" | sort -n | while read f; do
    echo "$f"
    profile_pup "$target_dir/$f" "$selector"
done

echo "[htmlq]"
find "$target_dir" -type f -name "*.html" -printf "%f\n" | sort -n | while read f; do
    echo "$f"
    profile_htmlq "$target_dir/$f" "$selector"
done
