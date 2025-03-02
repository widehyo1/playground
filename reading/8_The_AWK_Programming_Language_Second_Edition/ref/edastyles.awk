{ style[$8]++ }
END { for (i in style) print style[i], i }
