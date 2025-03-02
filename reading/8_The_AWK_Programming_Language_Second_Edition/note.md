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
