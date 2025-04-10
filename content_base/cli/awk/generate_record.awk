BEGIN {
    RS = ""
}
NR == 1{
    split($0, lines1, "\n")
    for (i = 1; i <= length(lines1); i++) {
        line1 = lines1[i]
        split(line1, seq_arr, "	")
        seq_info[i, 1] = seq_arr[1]
        seq_info[i, 2] = seq_arr[2]
        seq_info[i, 3] = seq_arr[3]
        seq_info[i, 4] = seq_arr[4]
    }
}
NR == 2{
    split($0, uuid_info_arr, "\n")
}
END {
    for (i = 1; i <= length(uuid_info_arr); i++) {
        report_seq = seq_info[i, 1]
        chart_seq = seq_info[i, 2]
        festival_seq = seq_info[i, 3]
        festival_series_number = seq_info[i, 4]
        print "("
        print "\"" uuid_info_arr[i] "\","
        print report_seq ","
        print chart_seq ","
        print festival_seq ","
        print festival_series_number ","
        print "\"2025-03-19 15:31:00.651322\","
        print "\"2025-03-19 15:31:00.651322\","
        print "\"9184a98e-8185-4900-b4ff-13ee64bfa45b\","
        print "\"9184a98e-8185-4900-b4ff-13ee64bfa45b\","
        print "),"
    }
}
