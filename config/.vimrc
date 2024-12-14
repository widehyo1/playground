set nocompatible               " turns off legacy vi mode
filetype off                   " required!

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVIm/Vundle.vim'
Plugin 'preservim/nerdtree', { 'on': 'NERDTreeToggle' }
Plugin 'nanotech/jellybeans.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'tpope/vim-fugitive'
Plugin 'majutsushi/tagbar'

call vundle#end()
filetype plugin indent on     " required!

"nerdtree
" autocmd VimEnter * NERDTree | wincmd p
autocmd VimEnter * if !&diff | NERDTree | wincmd p | endif
" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

set t_Co=256
colorscheme jellybeans

let mapleader=","

set number
set showmatch
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
set list
set listchars=tab:>-,trail:-
set nohlsearch
set clipboard=unnamedplus
set splitright
set splitbelow

nnoremap <leader>rc :e ~/.vimrc<CR>
nnoremap <leader>n :NERDTreeToggle<CR>
nnoremap <leader>a :NERDTreeFind<CR>

nnoremap <C-Right> gt
nnoremap <C-Left> gT
nnoremap <C-Up> :tabc<CR>
nnoremap <C-Down> :tabo<CR>
nnoremap <C-H> <C-W>h
nnoremap <C-L> <C-W>l
nnoremap <C-J> <C-W>j
nnoremap <C-K> <C-W>k
nnoremap <S-J> gt
nnoremap <S-K> gT
nnoremap <C-D> :sh<CR>
"nnoremap <C-D> :terminal<CR>i

imap jj <ESC>
