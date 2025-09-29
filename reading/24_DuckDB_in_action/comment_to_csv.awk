BEGIN {
  FS = "\""
  print "id,post_id,score,text,creation_date,user_id"
}
/row/ {
  if (index($8, ",")) {
    $8 = "\"" $8 "\""
  }
  printf "%s,%s,%s,%s,%s,%s\n",$2,$4,$6,$8,$10,$12
}
