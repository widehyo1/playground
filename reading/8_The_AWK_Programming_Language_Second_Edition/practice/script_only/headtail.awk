{
    line[NR] = $0
}
END {
    for (i = 1; i <= 3; i++) print line[i]
    print "..."
    for (i = NR-2; i <= NR; i++) print line[i]
}

