BEGIN {
    FS=","
    OFS=","
}
{
    "yes 'convert,it,to,your,favorite,format'" | getline str
    print str
    split(str, str_arr, " ")
    for (item in str_arr) {
        print item
        print str_arr[item]
        print $1,$2,$3,$4,$5
    }
}
