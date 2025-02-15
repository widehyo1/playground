function transform(format_str) {
    split(format_str, format_arr, ",")
    acc = ""
    format_arr[1] = $1
    format_arr[2] = "'" $2 "'"
    format_arr[3] = "'" $3 "'"
    format_arr[4] = "'" $4 "'"
    for (idx in format_arr) {
        if (idx != length(format_arr)) {
            acc = acc format_arr[idx] ","
        } else {
            acc = acc format_arr[idx]
        }
    }
    return acc
}
BEGIN {
    cmd = "wc -l < " ARGV[1]
    cmd | getline num_lines
    close(cmd)
    FS = ","
    OFS = ","
    format_str = "1,광평동,대한민국특수임무유공자회,구미시 구미대로 14길 7-5,36.107064,128.364115"
    print "INSERT INTO my_table(`연번`,`행정동`,`관리단체`,`설치장소(도로명주소)`,`위도`,`경도`) VALUES"
}
NR > 1 && NR < num_lines {
    row_str = transform(format_str)
    print "(" row_str "),"
}
NR == num_lines {
    row_str = transform(format_str)
    print "(" row_str ");"
}
