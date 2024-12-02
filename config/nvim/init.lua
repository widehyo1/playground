--[[ custom configuration ]]--

-- set leader key to comma
vim.g.mapleader = ','
-- esacpe key in insert mode
vim.keymap.set('i', 'jj', '<ESC>')
-- esacpe key in insert mode
vim.keymap.set("n", "<leader>rc", ':e ~/.config/nvim/init.lua<CR>')
--[[ nvim tree ]]--
-- toggle nvim tree
vim.keymap.set("n", "<leader>n", ':NvimTreeToggle<CR>')
vim.keymap.set("n", "<leader>a", ':NvimTreeFindFile<CR>')
-- manage window
vim.keymap.set('n', '<C-H>', '<C-W>h')
vim.keymap.set('n', '<C-J>', '<C-W>j')
vim.keymap.set('n', '<C-K>', '<C-W>k')
vim.keymap.set('n', '<C-L>', '<C-W>l')

-- basic settings
vim.opt.hlsearch = false
-- show line number
vim.opt.number = true
-- configurations with tab
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
-- convert tab to space
vim.opt.expandtab = true
-- visualize white characters
vim.opt.list = true
vim.opt.listchars = 'tab:>-,trail:-'

-- clipboard setting
-- install xclip
vim.opt.clipboard = 'unnamedplus'

--[[ lazy ]]--
require('config.lazy')
