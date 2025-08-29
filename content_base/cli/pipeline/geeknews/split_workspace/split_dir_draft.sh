#!/bin/bash

usage() {
  echo "Usage: ./split_dir [{-d|--directory} DIR] [{-p|--prefix} PREFIX] [{-l|--line} LINE] [--dest DEST]" >&2
  exit 1
}

basedir=$(basename $0)

directory=""
prefix=""
dest=""
line="1024"

while [[ $# -gt 0 ]]; do
  case "$1" in
    -d)
      shift
      directory="$1"
      ;;
    --directory)
      shift
      directory="$1"
      ;;
    -l)
      shift
      line="$1"
      ;;
    --line)
      shift
      line="$1"
      ;;
    -p)
      shift
      prefix="$1"
      ;;
    --prefix)
      shift
      prefix="$1"
      ;;
    --dest)
      shift
      dest="$1"
      ;;
    -*)
      usage
      ;;
    --*)
      if [[ -z "$dest" ]]; then
        dest="."
      else
        usage
      fi
      ;;
    *)
      usage
      ;;
  esac
  shift
done

if [[ -z "$directory" ]]; then
  usage
fi

directory=$(basename $(realpath "$directory"))

prefix=${prefix:-"$directory"}
dest=$(realpath ${dest:-$(basename $(realpath .))})

printf "directory: %s, prefix: %s, dest: %s, line: %s\n" "$directory" "$prefix" "$dest" "$line"
ls "$directory" | split -l "$line"  - "$prefix"

if [[ -ne "$dest" "$basedir" ]]; then
    mv "$prefix*" "$dest"
fi

find "$dest" -name "$prefix*" | while read f; do
    tarfile="$dest/$f.tgz"
    tar -czf "$tarfile" --directory "$dest" --files-from $f
    split_dir="$dest/dir_$f"
    mkdir "$split_dir"
    tar -xzf "$tarfile" --directory "$split_dir"
done
