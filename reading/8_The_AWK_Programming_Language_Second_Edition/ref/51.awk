# reverse - print input in reverse order by line (version 2)

    { line[NR] = $0 }  # remember each input line

END { for (i = NR; i > 0; i--)
          print line[i]
    }
