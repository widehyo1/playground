let mapleader=","

set number
set splitbelow
set splitright

nnoremap <C-D> <CMD>sh<CR>
inoremap jj <ESC>
tnoremap <C-Q> <C-\><C-N>

nnoremap <leader>so <CMD>so %<CR>
nnoremap <leader>term <CMD>terminal<CR>

nnoremap <leader>ws <CMD>split<CR>
nnoremap <leader>wns <CMD>new<CR>
nnoremap <leader>wv <CMD>vsplit<CR>
nnoremap <leader>wnv <CMD>vnew<CR>
nnoremap <C-L> <C-W>l
nnoremap <C-K> <C-W>k
nnoremap <C-J> <C-W>j
nnoremap <C-H> <C-W>h

nnoremap <leader>rc <CMD>e ~/.vimrc<CR>
nnoremap <leader>brc <CMD>e ~/.bashrc<CR>
nnoremap <leader>at <CMD>e ~/temp.txt<CR>
nnoremap <leader>as <CMD>e ~/script.awk<CR>
nnoremap <leader>ap <CMD>r ! awk -f ~/script.awk ~/temp.txt<CR>

nnoremap <leader>ct <CMD>e ~/request.json<CR>
nnoremap <leader>cs <CMD>e ~/script.curl<CR>
nnoremap <leader>cp <CMD>r ! curl --config ~/script.curl<CR>

