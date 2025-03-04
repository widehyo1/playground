`~/.vim/ftplugin/awk.vim`
```vim
iabbrev \begin; BEGIN {<CR><C-u>}
iabbrev \end; END {<CR><C-u>}
iabbrev \for; for (i = 1; i <= NF; i++) {}
iabbrev \forarr; for (idx in arr) {}
iabbrev \surr; function surround_str(str, start, end) {<CR>return start str end<CR>}
iabbrev \split; split(str, arr, sep)
iabbrev \strip; function strip(str) {<CR>gsub(regex, replace, str)<CR>return str<CR>}
iabbrev \join; function join(arr, sep) {<CR>acc = arr[1]<CR>for (i = 2; i <= length(arr); i++) {<CR>acc = acc sep arr[i]<CR>}<CR>return acc<CR>}

vnoremap gcc :s/^/# /<CR>
```

pr2-1
```awk
NR <= 6{
    line[NR] = $0
}
NR > 7 {
    if (NR % 3 == 0) {
        line[6] = $0
    } else if (NR % 3 == 1) {
        line[4] = $0
    } else {
        line[5] = $0
    }
}
END {
    if (NR <= 6) {
        for (i = 1; i <= NR; i++) print line[i]
    } else {
        offset = NR % 3
        print line[1]
        print line[2]
        print line[3]
        print "..."
        for (j = 0; j <= 2; j++) {
            index_offset = (offset + j) % 3
            print line[4 + index_offset]
        }
    }
}
```

```awk
{
  for (i = 1; i <= NF; i++) {
    field[i] += $i
  }
  if (NF > maxnf) {
    maxnf = NF
  }
}

END {
  for (i = 1; i <= maxnf; i++) {
    printf("%6g\t", field[i])
  }
  printf("\n")
}

```
  1111	  2220	  3300	  4000	     0	  6000	

bz0

awk '
{ s += $2; x[NR] = $2 }
END {
  for (i = NR-6; i <= NR; i++) w += x[i]
  for (i = NR-30; i <= NR; i++) m += x[i]
  for (i = NR-90; i <= NR; i++) q += x[i]
  for (i = NR-365; i <= NR; i++) yr += x[i]
  printf(" 7: %.0f 30: %.0f 90: %.0f 1yr: %.0f %.1fyr: %.0f\n",
    w/7, m/30, yr/365, NR/365, s/NR)
} ' $*


bz1

awk '
{ s += $2; x[NR] = $2; dist[int($2/2000)]++ }
END {
  for (i = NR-6; i <= NR; i++) w += x[i]
  for (i = NR-30; i <= NR; i++) m += x[i]
  for (i = NR-90; i <= NR; i++) q += x[i]
  for (i = NR-365; i <= NR; i++) yr += x[i]
  printf(" 7: %.0f 30: %.0f 90: %.0f 1yr: %.0f %.1fyr: %.0f\n",
    w/7, m/30, yr/365, NR/365, s/NR)

  scale = 0.05
  for (i = 1; i <= 10; i++) {
    printf("%5d: ", i*2000)
    for (j = 0; j < scale * dist[i]; j++) {
      printf("*")
    }
    printf("\n")
  }
} ' $*

