# check table with two fixed-width columns
#    Input:  two columns of eight-character integers
#    Output: rows in which second number is greater than first

{   if (NF == 1) {
        $1 = substr($0, 1, 8)
        $2 = substr($0, 9, 8)
    }
    if ($2 > $1)
        print "record", NR, "is bad: ", $0
}
