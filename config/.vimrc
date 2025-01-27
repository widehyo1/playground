set nocompatible              " be iMproved, required
filetype off                  " required
" git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
" set rtp+=~/.vim/bundle/Vundle.vim
" call vundle#begin()
" 
" Plugin 'VundleVim/Vundle.vim'
" Plugin 'preservim/nerdtree', { 'on': 'NERDTreeToggle' }
" Plugin 'nanotech/jellybeans.vim'
" Plugin 'vim-airline/vim-airline'
" Plugin 'vim-airline/vim-airline-themes' " 
" call vundle#end()            " required
filetype on

" jellybeans
" colorscheme jellybeans

" nerdtree
" autocmd VimEnter * NERDTree | wincmd p
" Exit Vim if NERDTree is the only window remaining in the only tab.
" autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

let mapleader=","

set number
set showmatch
set smartindent
set tabstop=4
set shiftwidth=4
set list
set listchars=tab:>-,trail:-
set expandtab
set clipboard=unnamedplus
set nohlsearch
set splitright
set splitbelow

nnoremap <leader>rc :e ~/.vimrc<CR>

nnoremap <C-H> <C-W>h
nnoremap <C-L> <C-W>l
nnoremap <C-J> <C-W>j
nnoremap <C-K> <C-W>k
" nnoremap <leader>a :NERDTreeFind<CR>
" nnoremap <leader>n :NERDTreeToggle<CR>
imap jj <ESC>
imap JJ <ESC>

nnoremap <C-D> :sh<CR>
" remove (carriage return) character
nnoremap <leader>d :%s/\r//g<CR>

let g:netrw_liststyle=3
" gh toggles dot files hide/show
nnoremap <leader>n :20Lex<CR>
