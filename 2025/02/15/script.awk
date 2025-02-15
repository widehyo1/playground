function join(arr, sep) {
    acc = arr[1]
    for (i = 2; i <= length(arr); i++) {
        acc = acc sep arr[i]
    }
    return acc
}
function strip(str) {
    gsub(/^\s+|\s+$/, res, str)
    return res
}
function transform_header(header_str) {
    split(header_str, header_arr, ",")
    header_arr[1] = "`" header_arr[1] "`"
    header_arr[2] = "`" header_arr[2] "`"
    header_arr[3] = "`" header_arr[3] "`"
    header_arr[4] = "`" header_arr[4] "`"
    header_arr[5] = "`" header_arr[5] "`"
    header_arr[6] = "`" header_arr[6] "`"
    result = join(header_arr, ",")
    return result
}
function transform_content(format_str) {
    split(format_str, format_arr, ",")
    format_arr[1] = $1
    format_arr[2] = "'" $2 "'"
    format_arr[3] = "'" $3 "'"
    format_arr[4] = "'" $4 "'"
    format_arr[5] = $5
    format_arr[6] = strip($6)
    result = join(format_arr, ",")
    return result
}
BEGIN {
    cmd = "wc -l < " ARGV[1]
    cmd | getline num_lines
    close(cmd)
    FS = ","
    OFS = ","
    header_str = "연번,행정동,관리단체,설치장소(도로명주소),위도,경도"
    format_str = "1,광평동,대한민국특수임무유공자회,구미시 구미대로 14길 7-5,36.107064,128.364115"
}
NR == 1 {
    header = ""
    insert_str = transform_header(header_str)
    print "INSERT INTO my_table(" insert_str ") VALUES"
}
NR > 1 && NR < num_lines {
    row_str = transform_content(format_str)
    print "(" row_str "),"
}
NR == num_lines {
    row_str = transform_content(format_str)
    print "(" row_str ");"
}
