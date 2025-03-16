let menu_list = map(filter(range(1, bufnr('$')), 'buflisted(v:val)'), 'v:val . " " .  bufname(v:val)')

function! MenuSelected(id, result) abort
  echo a:id . " " . a:result
endfunction
let menu = popup_menu(menu_list, #{ title: 'buffer list', callback: 'MenuSelected', })
