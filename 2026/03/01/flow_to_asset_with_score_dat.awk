function strip(str) {
  gsub(/^\s+|\s+$/, "", str)
  return str
}

BEGIN {
  FS = ","
  OFS = ","
}

NR == 1{
  print "data,asset,net income,score,expanse"
  next
}
{
  gsub("\"","",$8)
  $8 = strip($8)
  print $1,$2,$3+$4+$5+$6,$7,$8 ? $8 : ""
}
