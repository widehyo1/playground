function! CaptureCommandOutputToClipboard(cmd)
    redir @"
    silent execute a:cmd
    redir END
    let @+ = @"
endfunction
nnoremap <leader>path :call CaptureCommandOutputToClipboard('echo fnamemodify(expand("%"), ":~:.")')<CR>
