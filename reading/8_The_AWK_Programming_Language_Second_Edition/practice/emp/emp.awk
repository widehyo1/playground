# $3 > 0 {
#     print $1, $2 * $3
# }

# $3 == 0 {
#     print $1
# }

# {
#     print $1
# }

# {
#     print NF, $1, $NF
# }

# {
#     print NR, $0
# }

# {
#     print "total pay for", $1, "is", $2 * $3
# }

# {
#     printf("total pay for %s is $%.2f\n", $1, $2 * $3)
# }

# {
#     printf("%-8s $%6.2f\n", $1, $2 * $3)
# }

# awk '{ printf("$%6.2f %s\n", $2 * $3, $0) }' emp.data | sort

# $2 >= 20

# $2 * $3 > 200 {
#     printf("$%.2f for %s\n", $2 * $3, $1)
# }

# $1 == "Susie"

# $2 >= 20 || $3 >= 20

# $2 >= 20
# $3 >= 20

# !($2 < 20 && $3 < 20)

# NF != 3 { print $0, "number of fields is not equal to 3" }
# $2 < 15 { print $0, "rate is too low" }
# $2 > 25 { print $0, "rate exceeds $25 per hour" }
# $3 < 0  { print $0, "nagative hours worked" }
# $3 > 60 { print $0, "too may hours worked" }

# BEGIN { print "NAME RATE    HOURS"; print "" }
# { print }

# $3 > 15 {
#     emp = emp + 1 # emp++
# }
# END {
#     print emp, "employees worked more than 15 hours"
# }

# END {
#     print NR, "employees"
# }

# $2 > maxrate { maxrate = $2; maxemp = $1 }
# END { print "highest hourly rate:", maxrate, "for", maxemp }

# { names = names $1 " "}
# END { print names }

# END { print }

# { print $1, length($1) }

# { nc += length($0) + 1
#   nw += NF
# }
# END { print NR, "lines,", nw, "words,", nc, "characters" }

# $2 > 30 { n++; pay += $2 * $3 }
# END {
#     if (n > 0) {
#         print n, "high-pay employees, total pay is", pay,
#                  " average pay is", pay/n
#     } else {
#         print "No employees are paid more than $30/hour"
#     }
# }

# {
#     line[NR] = $0
# }
# END {
#     i = NR
#     while (i > 0) {
#         print line[i]
#         i--
#     }
# }

# {
#     line[NR] = $0
# }
# END {
#     for (i = NR; i > 0; i--) {
#         print line[i]
#     }
# }

# END { print NR }
# NR <= 10
# NR == 10
# NR % 10 == 1
# { print $NF }
# END { print $NF }
# NF > 4
# NF != 4
# $NF > 4

# { nf += NF }
# END { print nf}

# /Beth/ { nlines++ }
# END { print nlines }

# $1 > max { max = $1; maxline = $0 }
# END { print max, maxline }

# NF > 0
# length($0) > 80
# { print NF, $0 }
# { print $2, $1 }
# { temp = $1; $1 = $2; $2 = temp; print }
# { print NR, $0 }
# { $1 = NR; print }
# { $2 = ""; print }

# { for (i = NF; i > 0; i--) printf("%s ", $i)
#   printf("\n")
# }

# { sum = 0
#   for (i = 1; i <= NF; i++) sum += $i
#   print sum
# }

{ for (i = 1; i <= NF; i++) sum += $i }
END { print sum }
