# print countries with column headers and totals

BEGIN { FS = "\t"   # make tab the field separator
        printf("%12s %6s %5s   %s\n\n",
              "COUNTRY", "AREA", "POP", "CONTINENT")
      }
      { printf("%12s %6d %5d   %s\n", $1, $2, $3, $4)
        area += $2
        pop += $3
      }
END   { printf("\n%12s %6d %5d\n", "TOTAL", area, pop) }
