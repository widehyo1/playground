BEGIN {
    RS = ""
    OFS = "|"
    print "topic|theme|main_summary|sub_summary"
}
{
    split($0, lines, "\n")
    for (idx in lines) {
        if (idx == 1) {
            topic = substr(lines[idx], 7)
        }
        if (lines[idx] ~ /^-/) {
            theme = substr(lines[idx], 3)
        }
        if (lines[idx] ~ /^  -/) {
            main_summary = substr(lines[idx], 5)
        }
        if (lines[idx] ~ /^    -/) {
            sub_summary = substr(lines[idx], 7)
            print topic,theme,main_summary,sub_summary
        }
    }
}
