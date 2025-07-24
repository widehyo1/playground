function printRow(topic, theme, main_summary, sub_summary) {
  print topic,theme,main_summary,sub_summary
}

BEGIN {
  RS = ""
  FS = "\n"
  print "topic|theme|main_summary|sub_summary"
}

{
  topic = substr($1, 7)
  for (i = 2; i <= NF; i++) {
    if (match($i, /^-/))     theme        = substr($i, 3); continue
    if (match($i, /^  -/))   main_summary = substr($i, 5); continue
    if (match($i, /^    -/)) sub_summary  = substr($i, 7); printRow(topic, theme, main_summary, sub_summary)
  }
}
