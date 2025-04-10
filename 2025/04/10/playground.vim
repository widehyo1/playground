function! ShowCmdOutputInPopup()
  " Run the command and capture its output as a list of lines.
  let lines = system('PAGER=cat python -m pydoc sum')
  let popup_content = lines->split('\n')

  " Determine the popup dimensions relative to the editor size.
  let width  = float2nr(&columns * 0.8)
  let height = float2nr(&lines * 0.8)


  let start_row  = float2nr(&lines * 0.1)
  let start_col = float2nr(&columns* 0.1)

  " Set popup options:
  " - 'line' and 'col' positions relative to the cursor.
  " - 'minwidth'/'maxwidth' and 'minheight'/'maxheight' keep it fixed sized.
  " - 'scrollbar' adds a vertical scrollbar.
  " - 'border' and 'padding' customize the look.
  let opts = {
        \ 'line': start_row,
        \ 'col': start_col,
        \ 'minwidth': width,
        \ 'minheight': height,
        \ 'maxwidth': width,
        \ 'maxheight': height,
        \ 'scrollbar': 1,
        \ 'border': [],
        \ 'padding': [0,1,0,1]
        \ }

  " Create and show the popup window.
  call popup_create(popup_content, opts)
endfunction

" Create a command to call the function.
" command! FloatCmd call ShowCmdOutputInPopup('ls')
command! FloatCmd call ShowCmdOutputInPopup()
