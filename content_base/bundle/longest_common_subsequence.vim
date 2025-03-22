function! GetLoadedBufferList()
  let l:buf_info = getbufinfo()
  let l:listed_buffer_info = l:buf_info
        \ ->filter({_, val -> val.listed == 1 })
        \ ->map({_, val -> {'bufnr': val.bufnr, 'name': val.name}})
  return l:listed_buffer_info
endfunction

function! GetSmithWatermanScore(search_word, buf_name)
  let l:tx = ' ' . a:search_word
  let l:ty = ' ' . a:buf_name

  " direction
  let l:up      = 0b001
  let l:left    = 0b010
  let l:upleft  = 0b100
  let l:default = 0b000

  let l:matrix = []
  let l:highest_scored_position_list = []
  let l:score = 0

  function! CalcElement(row, col, match = 3, mis_match = -3, gap_panalty = -2) closure
    " closure for calculate matrix element with free variables:
    " l:matrix, l:highest_scored_position_list, l:score, l:tx, l:ty
    " l:up, l:left, l:upleft, l:default

    " echo 'CalcElement (row: ' . a:row ', col: ' . a:col . ') len(l:matrix) is ' . len(l:matrix) . ' len(l:matrix[0]) is ' . len(l:matrix[0])

    if a:row == 0
      return 0
    elseif a:col == 0
      return 0
    endif

    let l:up_value = l:matrix[a:row - 1][a:col][0]
    let l:left_value = l:matrix[a:row][a:col - 1][0]
    let l:diag_value = l:matrix[a:row - 1][a:col - 1][0]

    let l:up_candidate = l:up_value + a:gap_panalty
    let l:left_candidate = l:left_value + a:gap_panalty

    let l:diag_candidate = l:diag_value + a:mis_match

    if l:tx[a:row] == l:ty[a:col]
      let l:diag_candidate = l:diag_value + a:match
    endif

    let l:element_value = max([l:up_candidate, l:left_candidate, l:diag_candidate])
    let l:element_direction = l:default

    if l:element_value < 0
      let l:matrix[a:row][a:col] = [0, 0]
      return 0
    endif

    if l:element_value == l:up_candidate
      let l:element_direction = or(l:element_direction, l:up)
    endif
    if l:element_value == l:left_candidate
      let l:element_direction = or(l:element_direction, l:left)
    endif
    if l:element_value == l:diag_candidate
      let l:element_direction = or(l:element_direction, l:upleft)
    endif

    let l:matrix[a:row][a:col] = [l:element_value, l:element_direction]

    if l:element_value > l:score
      if len(l:highest_scored_position_list) > 0
        call remove(l:highest_scored_position_list, 0, len(l:highest_scored_position_list)-1)
      endif
      call add(l:highest_scored_position_list, [a:row, a:col])
      return l:element_value
    elseif l:element_value == l:score
      call add(l:highest_scored_position_list, [a:row, a:col])
      return l:element_value
    else
      return l:score
    endif
  endfunction


  " initialize matrix
  for i in range(len(l:tx))
      let l:matrix_row = []
      for j in range(len(l:ty))
        call add(l:matrix_row, [0,0])
      endfor
      call add(l:matrix, l:matrix_row)
  endfor

  for i in range(len(l:tx))
    for j in range(len(l:ty))
      let l:score = CalcElement(i, j)
    endfor
  endfor

  let l:buf_name_position_list = []

  while len(l:highest_scored_position_list) > 0
    let l:cur_position = remove(l:highest_scored_position_list, -1)
    let [l:cur_row, l:cur_col] = l:cur_position
    let [l:cur_value, l:cur_direction] = l:matrix[l:cur_row][l:cur_col]

    if l:cur_value == 0
      break
    endif

    if and(l:cur_direction, l:up) > 0
      call add(l:highest_scored_position_list, [l:cur_row - 1, l:cur_col])
    endif
    if and(l:cur_direction, l:left) > 0
      call insert(l:buf_name_position_list, l:cur_col)
      call add(l:highest_scored_position_list, [l:cur_row, l:cur_col - 1])
    endif
    if and(l:cur_direction, l:upleft) > 0
      call insert(l:buf_name_position_list, l:cur_col)
      call add(l:highest_scored_position_list, [l:cur_row - 1, l:cur_col - 1])
    endif

    break
  endwhile

  return [l:score, l:buf_name_position_list]
endfunction

function! PopupBuffer()

  " Function to capture and echo the text in the search buffer
  function! CaptureSearchText() closure
    " Get the content of the search buffer
    let l:text = join(getline(1,1), '')
    " Echo the content to the command line
    let l:search_word = l:text
    if l:search_word == ''
      call RedrawBufferList(l:buffer_info_list)
    else
      call SmithWaterman(l:search_word, l:buffer_info_list)
    endif
  endfunction

  function! SmithWaterman(search_word, buffer_info_list) closure
    " echo l:search_word
    let l:filtered_buffer_list = copy(a:buffer_info_list)
          \ ->filter({_, val -> GetSmithWatermanScore(a:search_word, val.name)[0] > 0})
    call RedrawBufferList(l:filtered_buffer_list)
  endfunction

  function! RedrawBufferList(buffers) closure
    let l:header = []
    let l:lines = []
    for idx in range(len(a:buffers))
      let l:buffer = a:buffers[idx]
      let l:bufnr = l:buffer.bufnr
      let l:bufname = l:buffer.name
      call add(l:lines, l:bufname)
    endfor

    execute 'buffer' . l:pop_bufnr
    setlocal modifiable
    call setbufline(l:pop_bufnr, 1, l:header + l:lines)
    setlocal nomodifiable
  endfunction

  let l:search_word = ""
  let l:buffer_info_list = GetLoadedBufferList()

  new
  let l:pop_bufnr = bufnr()
  setlocal buftype=nofile
  setlocal noswapfile
  setlocal nobuflisted
  setlocal nomodifiable
  resize 20

  new
  let l:search_bufnr = bufnr()
  setlocal buftype=nofile
  setlocal filetype=search
  setlocal noswapfile
  setlocal nobuflisted
  resize 1

  " echo l:pop_bufnr . ' ' . ' ' . l:search_bufnr
  call RedrawBufferList(l:buffer_info_list)

  redraw

  " Create an autocommand for TextChangedI in the 'search' buffer
  autocmd TextChangedI <buffer> call CaptureSearchText()

endfunction


call PopupBuffer()
