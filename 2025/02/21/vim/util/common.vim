" Function to process the visual selection with awk and copy output to clipboard
function! ProcessVisual()
  " Save the current unnamed register content and type.
  let l:old_reg   = getreg('"')
  let l:old_regtype = getregtype('"')

  " Get the visually selected lines and join them into a single string.
  let l:sel = join(getline("'<", "'>"), "\n")

  " Run the awk script on the selected text.
  let l:result = system('awk -f ~/script.awk', l:sel)

  " Copy the result to the clipboard register.
  call setreg('+', l:result)

  " Optionally restore the unnamed register (if you need it later).
  call setreg('"', l:old_reg, l:old_regtype)

  " Provide feedback.
  echo "Processed text copied to clipboard"
endfunction

function! CaptureCommandOutputToClipboard(cmd)
    redir @"
    execute a:cmd
    redir END
    let @+ = @"
endfunction

function! ToggelAutoIndent()
    if &autoindent
        set noautoindent
        set autoindent?
    else
        set autoindent
        set autoindent?
    endif
endfunction
nnoremap <leader>togai :call ToggelAutoIndent()<CR>

