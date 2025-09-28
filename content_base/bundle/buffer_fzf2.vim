function! GetLoadedBufferList()
  let buf_info = getbufinfo()
  let listed_buffer_info = map(filter(buf_info, 'v:val.listed == 1'), {
        \   'bufnr': v:val.bufnr,
        \   'name' : fnamemodify(expand(v:val.name), ":~:.")
        \ })
  return listed_buffer_info
endfunction

function! GetSmithWatermanScore(search_word, buf_name)
  let tx = ' ' . a:search_word
  let ty = ' ' . a:buf_name

  " direction
  let up      = 0b001
  let left    = 0b010
  let upleft  = 0b100
  let default = 0b000

  let matrix = []
  let highest_scored_position_list = []
  let score = 0

  function! CalcElement(row, col, match = 3, mis_match = -3, gap_panalty = -2) closure
    " closure for calculate matrix element with free variables:
    " matrix, highest_scored_position_list, score, tx, ty
    " up, left, upleft, default

    let up_value = matrix[a:row - 1][a:col][0]
    let left_value = matrix[a:row][a:col - 1][0]
    let diag_value = matrix[a:row - 1][a:col - 1][0]

    let up_candidate = up_value + a:gap_panalty
    let left_candidate = left_value + a:gap_panalty

    let diag_candidate = diag_value + a:mis_match

    if tx[a:row] == ty[a:col]
      let diag_candidate = diag_value + a:match
    endif

    let element_value = max([up_candidate, left_candidate, diag_candidate])
    let element_direction = default

    if element_value < 0
      let matrix[a:row][a:col] = [0, 0]
      return max([score, element_value])
    endif

    if element_value == up_candidate
      let element_direction = or(element_direction, up)
    endif
    if element_value == left_candidate
      let element_direction = or(element_direction, left)
    endif
    if element_value == diag_candidate
      let element_direction = or(element_direction, upleft)
    endif

    let matrix[a:row][a:col] = [element_value, element_direction]

    if element_value > score
      if len(highest_scored_position_list) > 0
        call remove(highest_scored_position_list, 0, len(highest_scored_position_list)-1)
      endif
      call add(highest_scored_position_list, [a:row, a:col])
      return max([score, element_value])
    elseif element_value == score
      call add(highest_scored_position_list, [a:row, a:col])
      return max([score, element_value])
    else
      return max([score, element_value])
    endif
  endfunction

  " initialize matrix
  for i in range(len(tx))
      let matrix_row = []
      for j in range(len(ty))
        call add(matrix_row, [0,0])
      endfor
      call add(matrix, matrix_row)
  endfor

  for i in range(1, len(a:search_word))
    for j in range(1, len(a:buf_name))
      let score = CalcElement(i, j)
    endfor
  endfor

  let buf_name_position_list = []

  while len(highest_scored_position_list) > 0
    let cur_position = remove(highest_scored_position_list, -1)
    let [cur_row, cur_col] = cur_position
    let [cur_value, cur_direction] = matrix[cur_row][cur_col]

    if cur_value == 0
      break
    endif

    if and(cur_direction, up) > 0
      call insert(buf_name_position_list, -1)
      call add(highest_scored_position_list, [cur_row - 1, cur_col])
    endif
    if and(cur_direction, left) > 0
      call insert(buf_name_position_list, cur_col - 1)
      call add(highest_scored_position_list, [cur_row, cur_col - 1])
    endif
    if and(cur_direction, upleft) > 0
      call insert(buf_name_position_list, cur_col - 1)
      call add(highest_scored_position_list, [cur_row - 1, cur_col - 1])
    endif
  endwhile

  return [score, buf_name_position_list]
endfunction

function! GetHighlightPosition(position)
  let flag = 0
  let prev = -1
  let start = -1
  let result = []
  for pos in a:position
    if flag
      if pos - prev == 1
        let prev = pos
      else
        let flag = 0
        call add(result, [start, pos])
      endif
    else
      let start = pos
      let prev = pos
      let flag = 1
    endif
  endfor
  if flag
    call add(result, [start, a:position[-1]])
  endif
  return result
endfunction

function! DecorateText(text, position_list)
  let result_text = ""
  let idx = 0
  for [start, end] in a:position_list
    let result_text = a:text[idx:start - 1] . '[' . a:text[start:end] . ']'
    let idx = end + 1
  endfor
  if idx != len(a:text)
    let result_text = result_text . a:text[idx:]
  endif
  return result_text
endfunction

function! ScoreSortKey(lhs, rhs)
  return a:rhs.score - a:lhs.score
endfunction

function! Helper(pop_bufnr, search_bufnr, contents)
  let is_search_buf = bufnr() == a:search_bufnr

  let head = a:contents[0]
  let ct = copy(a:contents)
  if has_key(head, 'decorated_text')
    let ct = filter(ct, {_, val -> val.score > 0})
    let ct = sort(ct, 'ScoreSortKey')
    let lines = copy(ct)
          \ ->map({_, val -> val.score . '	' . val.decorated_text})
  else
    let lines = copy(ct)
          \ ->map({_, val -> val.name})
  endif

  execute 'buffer!' . a:pop_bufnr
  setlocal modifiable
  normal ggdG
  call setbufline(a:pop_bufnr, 1, lines)
  setlocal nomodifiable

  if is_search_buf
    execute 'buffer!' . a:search_bufnr
    call cursor(1, 9999)
  endif
  redraw
  return ct[0].bufnr
endfunction

function! PopupBuffer()

  " Function to capture and echo the text in the search buffer
  function! CaptureSearchText() closure
    " Get the content of the search buffer
    let search_buffer_lines = getline(1,'$')
    if len(search_buffer_lines) > 1
      execute 'quit!'
      execute 'quit!'
      execute 'buffer! ' . target_bufnr
      return
    endif
    let search_word = join(getline(1,1), '')
    " initialize temp register
    if search_word == ''
      call RedrawBufferList(buffer_info_list, 0)
    else
      call SmithWaterman(search_word, buffer_info_list)
    endif
  endfunction

  function! SmithWaterman(search_word, buffer_info_list) closure
    let filtered_buffer_list = []
    for buffer_info in copy(a:buffer_info_list)
      let [score, position] = GetSmithWatermanScore(a:search_word, buffer_info.name)
      if score > 0
        let hlpos = GetHighlightPosition(position)
        let target_buf_info = {}
        let target_buf_info.score = score
        let target_buf_info.hlposition = hlpos
        let target_buf_info.decorated_text = DecorateText(buffer_info.name, hlpos)
        let target_buf_info = extend(target_buf_info, buffer_info)
        call add(filtered_buffer_list, target_buf_info)
      endif
    endfor

    call RedrawBufferList(filtered_buffer_list, 1)
  endfunction

  function! RedrawBufferList(buffers, flag) closure

    let buf_len = len(a:buffers)

    if a:flag == 0

      if buf_len == 0
        let target_bufnr = Helper(pop_bufnr, search_bufnr, target_buffer_list)
        return
      endif

      let target_buffer_list = copy(a:buffers)
      let target_bufnr = Helper(pop_bufnr, search_bufnr, target_buffer_list)
      return
    else
      let target_buffer_list = [{'name': 'there is no searched buffer', 'bufnr': -1}]
      if buf_len == 0
        let target_bufnr = Helper(pop_bufnr, search_bufnr, target_buffer_list)
        return
      endif
      let target_buffer_list = copy(a:buffers)
      let target_bufnr = Helper(pop_bufnr, search_bufnr, target_buffer_list)
      return
    endif
  endfunction

  let search_word = ''
  let buffer_info_list = GetLoadedBufferList()
  let target_buffer_list = [{'name': 'there is no loaded buffer', 'bufnr': -1}]
  let target_bufnr = -1

  new
  let pop_bufnr = bufnr()
  setlocal buftype=nofile
  setlocal filetype=bufpop
  setlocal noswapfile
  setlocal nobuflisted
  setlocal nomodifiable
  resize 20

  new
  let search_bufnr = bufnr()
  setlocal buftype=nofile
  setlocal filetype=search
  setlocal noswapfile
  setlocal nobuflisted
  resize 1

  " echo pop_bufnr . ' ' . ' ' . search_bufnr
  call RedrawBufferList(buffer_info_list, 0)

  redraw

endfunction


call PopupBuffer()
