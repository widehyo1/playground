BEGIN {
    RS = ""
    FS = "\n"
}
NR % 2 == 1 {
    for (i = 1; i <= NF; i++) {
        temp[NR + 1][i] = $i
    }
}

NR % 2 == 0 {
    for (i in temp[NR]) {
        val = temp[NR][i]
        tot[val] = $i
        tot[$i] = val
    }
}
END {
    for (idx in tot) {
        print "tot[\"" idx "\"]=\"" tot[idx] "\""
    }
}

