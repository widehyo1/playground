function strip(str) {
  gsub(/^\s+|\s+$/, "", str)
  return str
}

/amount/ {
  if ($0 ~ /text/) {
    split($0, arr, "\"")
    for (i = 1; 2 * i <= length(arr); i++) {
      text_data[i] = arr[2 * i]
    }
  } else {
    gsub("),", "", $0)
    split($0, arr, ",")
    data[1] = strip(substr(arr[1], index(arr[1], "(") + 1))
    for (i = 2; i <= length(arr); i++)
      data[i] = strip(arr[i])
  }
}

/title/ {
  if ($0 ~ /short/) next
  split($0, arr, "\"")
  for (i = 1; 2 * i <= length(arr); i++) {
    titles[i] = arr[2 * i]
  }
}

END {
  # for (i in data)
  #   print "data[" i "] = " data[i]
  # for (i in text_data)
  #   print "text_data[" i "] = " text_data[i]
  # print "data|text_data"
  # for (i = 1; i <= length(data); i++) {
  #   print data[i] "|" text_data[i]
  # }

  # for (i in titles)
  #   print "titles[" i "] = " titles[i]
  print "rank,title,weekly amount(million USD)"
  for (i = 1; i <= length(data); i++) {
    printf "%s,%s,%s\n", i, titles[i], data[i]/1000000
  }
}
