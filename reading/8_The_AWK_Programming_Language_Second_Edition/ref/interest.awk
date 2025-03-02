# interest computation:
# input:  amount  rate  years
# output: compounded value

{   i = 1
    while (i <= $3) {
        print $1 * (1 + $2) ^ i
        i = i + 1
    }
}
