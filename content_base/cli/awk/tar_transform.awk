BEGIN {
  FS = "\n"
  RS = ""
  printf "tar -czvf transform.tgz "
}
NR == 1 {
  # print NR
  # print ""
  for (i = 1; i <= NF; i++) {
    # print $i
    visited[arr[split($i, arr, "/")]] = $i
  }
}
NR == 2 {
  # print NR
  # print ""
  for (i = 1; i <= NF; i++) {
    # print $i
    key = arr[split($i, arr, "/")]
    value = visited[arr[split($i, arr, "/")]]
    if (value) {
      printf "--transform 's|%s|%s|' \\\n", value, $i
    }
  }
}

END {
  for (idx in visited) {
    # printf "idx: %s, visited[idx]: %s\n", idx, visited[idx]
    if (visited[idx]) {
      printf "%s \\\n", visited[idx]
    }
  }
}
