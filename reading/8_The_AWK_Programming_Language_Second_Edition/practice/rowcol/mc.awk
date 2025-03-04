```awk
{ out = sprintf("%s%-10.10s  ", out, $0)
  if (++n >= 5) {
    print substr(out, 1, length(out)-2)
    out = ""
    n = 0
  }
}
END {
  if (n > 0)
    print substr(out, 1, length(out)-2)
}
```

```awk
{ lines[NR] = $0
  if (length($0) > max)
    max = length($0)
}
END {
  fmt = sprintf("%%-%d.%ds", max, max)
  ncol = int(60 / (max+2) + 0.5)
  for (i = 1; i <= NR; i += ncol) {
    out = ""
    for (j = i; j < i+ncol && j <= NR; j++) {
      out = out sprintf(fmt, lines[j]) " "
    }
    sub(/ +$/, "", out)
    print out
  }
}
```

Alice       Archie      Eva         Liam        Louis     
Mary        Naomi       Rafael      Sierra      Sydney    

Alice  Archie Eva    Liam   Louis  Mary   Naomi  Rafael
Sierra Sydney

6
%-6.6s
Alice  Archie Eva    Liam   Louis  Mary   Naomi  Rafael
Sierra Sydney
