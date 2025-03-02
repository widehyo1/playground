    { nc += length($0) + 1
      nw += NF
    }
END { print NR, "lines,", nw, "words,", nc, "characters" }
