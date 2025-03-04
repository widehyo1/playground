BEGIN {
    n = ARGV[1]
}
{
    position = NR % n
    line[position] = $0
}
END {
    if (NR <= n) {
        for (idx in line) {
            print line[idx]
        }
    } else {
        for (j = 0; j <= n - 1; j++) {
            temp_arr[j] = line[(n + position - j) % n]
        }
        for (k = n - 1; k >= 0; k--) {
            print temp_arr[k]
        }
    }
}
