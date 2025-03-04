NR <= 3 {
    print; next
}
{
    line[NR%3] = $0
}
END {
    print "..."
    i = (NR+1) % 3
    for (j = 1; j <= 3; j++) {
        print line[i]
        i = (i+1) % 3
    }
}

