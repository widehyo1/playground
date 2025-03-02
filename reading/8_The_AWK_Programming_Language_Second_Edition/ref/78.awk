{ sum = 0
  for (i = 1; i <= NF; i++) sum = sum + $i
  print sum
}
