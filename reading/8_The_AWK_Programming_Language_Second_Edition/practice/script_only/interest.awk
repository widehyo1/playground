# { i = 1
#   while (i <= $3) {
#     printf("\t%.2f\n", $1 * (1 + $2) ^ i)
#     i++
#   }
# }

{
    for (i = 1; i <= $3; i++)
        printf("\t%.2f\n", $1 * (1 + $2) ^ i)
}
