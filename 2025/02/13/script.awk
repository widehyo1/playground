BEGIN {
    q="'"
    FS=","
    OFS=":"
}
{
    # print $0
    # print $1,$2,$3
    for (i = 1; i <= NF; ++i) {
        printf("%s %s%s", i, $i, OFS)
        printf("|")
        printf("%s%s%s", q, $i, q)
    }
    printf("\n")
}
