function! SnakeToCamel(text)
  let l:lst = split(a:text, '_')
  let l:camel = l:lst[0]
  for l:item in l:lst[1 :]
    let l:camel = l:camel . toupper(l:item[0]) . l:item[1 :]
  endfor
  return l:camel
endfunction

function! CamelToSnake(text)
  let l:text = substitute(a:text, '^_+', '', '')
  return substitute(l:text, '\(\u\)', '_\L\1', 'g')
endfunction

" let text = 'longestCommonSubstring'
" let text = 'longest_common_substring'
" let text = 'longestCommonSubstring'
let text = 'LongestCommonSubstring'
" echo match(text, '[[:upper:]]', 0, 2)
"
echo match(text, '[[:upper:]]') >= 0
