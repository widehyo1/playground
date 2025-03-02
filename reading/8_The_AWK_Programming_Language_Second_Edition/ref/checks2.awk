# print check information

BEGIN         { RS = ""; FS = "\n" }
/(^|\n)check/ { printf("%8s %5d %8s  %s\n",
                    field("date"),
                    field("check"),
                    sprintf("$%.2f", field("amount")),
                    field("to"))
              }

function field(name,   i,f) {
    for (i = 1; i <= NF; i++) {
        split($i, f, "\t")
        if (f[1] == name)
            return f[2]
    }
    printf("error: no field %s in record\n%s\n", name, $0)
}
