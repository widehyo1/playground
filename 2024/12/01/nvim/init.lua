--[[ nvim-tree ]]--

--[[
-- disable netrw at the very start of your init.lua
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

-- optionally enable 24-bit colour
vim.opt.termguicolors = true

-- empty setup using defaults
require('nvim-tree').setup()

-- OR setup with some options
require('nvim-tree').setup({
    sort = {
        sorter = 'case_sensitive',
    },
    view = {
        width = 30,
    },
    renderer = {
        group_empty = true,
    },
    filters = {
        dotfiles = true,
    },
})
]]--


--[[ lazy ]]--
require('config.lazy')

-- local function get_plugins(dirs)
--     local plugins = {}
--     for _, dirs in ipairs(dirs) do
--         local path = table.concat({ vim.fn.stdpath('config'), 'lua', 'plugins', dir }, '/')
--         for fname in vim.fs.dir(path) do
--             local n = fname:match("^(.*)%.lua$")
--             table.insert(plugins, require(table.concat({ 'plugins', dir, n}, '.')))
--         end
--     end
--     return plugins
-- end
-- 
-- local function setup(plugins)
--     local lazy = require('lazy')
--     return lazy.setup(plugins)
-- end
-- 
-- setup(get_plugins({ }))

-- Setup lazy.nvim
-- require('lazy').setup({
--     spec = {
--         -- import your plugins here
--     },
--     -- Configure any other settings here. See the documentation for more details.
--     -- colorscheme that will be used when installing plugins.
--     install = { colorscheme = { 'habamax' } },
--     -- authmatically check for plugin updates
--     checker = { enabled = true },
-- })
-- Make sure to setup `mapleader` and `maplocalleader` before
-- loading lazy.nvim so that mappings are correct.
-- This is also a goot place to setup other settings (vim.opt)
-- vim.g.mapleader = ','
-- vim.g.maplocalleader = '\\'
-- ]]--

--[[ custom configuration ]]--

-- set leader key to comma
vim.g.mapleader = ','
-- esacpe key in insert mode
vim.keymap.set('i', 'jj', '<ESC>')
-- esacpe key in insert mode
vim.keymap.set("n", "<leader>rc", ':e ~/.config/nvim/init.lua<CR>')

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

--[[
-- set leader key to comma
vim.g.mapleader = ','

-- vim.g.mapleader = ' '
-- vim.g.maplocalleader = '\\'
-- esacpe key in insert mode
vim.keymap.set('i', 'jj', '<ESC>')
-- esacpe key in insert mode
vim.keymap.set("n", "<leader>rc", ':e ~/.config/nvim/init.lua<CR>')

-- clipboard setting
if string.find(vim.uv.os_uname().release, 'microsoft') ~= nil then
    vim.api.nvim_create_autocmd({ "TextYankPost" }, {
        pattern = "*",
        callback = function()
            vim.system({ '/mnt/c/windows/system32/clip.exe' }, { stdin = vim.trim(vim.fn.getreg('"')) })
        end,
    })
end

-- local osc52 = require("vim.ui.clipboard.osc52")
-- vim.g.clipboard = {
--   name = "OSC-52",
--   copy = {
--     ["+"] = osc52.copy("+"),
--     ["*"] = osc52.copy("*"),
--   },
--   paste = {
--     ["+"] = osc52.paste("+"),
--     ["*"] = osc52.paste("*"),
--   },
-- }
-- 
-- local silent_noremap = { silent = true, noremap = true }
-- vim.keymap.set('n', '<leader>y', '"+y', silent_noremap)
-- vim.keymap.set('v', '<leader>y', '"+y', silent_noremap)
-- 
-- vim.keymap.set('n', '<leader>d', '"+d', silent_noremap)
-- vim.keymap.set('v', '<leader>d', '"+d', silent_noremap)
-- vim.keymap.set('n', '<leader>D', '"+D', silent_noremap)
-- 
-- vim.keymap.set('n', '<leader>p', '"+p', silent_noremap)

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

-- custom utils
function terminal_to_buffer()
    print('terminal_to_buffer')
    local prev_buffer_number = vim.g.restore_bufnr
    print('prev_buffer_number: ' .. prev_buffer_number)
    if not prev_buffer_number then
        print('flag')
        return
    end
    -- pritn(prev_buffer_number)
    -- local buffer_number = vim.api.nvim_get_current_buf()
    -- print(buffer_number)
    -- vim.g.restore_bufnr = buffer_number
    -- print(vim.g.restore_bufnr)
    local win = vim.api.nvim_get_current_win()
    print('win: ' .. win .. ' prev_buffer_number: ' .. prev_buffer_number)
    vim.api.nvim_win_set_buf(win, prev_buffer_number)
end

vim.api.nvim_create_autocmd({ "TermOpen" }, {
    callback = function()
        vim.g.restore_bufnr = vim.api.nvim_get_current_buf()
        print('vim.g.restore_bufnr is saved:: ' .. vim.g.restore_bufnr) 
    end
})

treesitter_utils = require('treesitter_utils')

vim.keymap.set('n', '<leader>t', treesitter_utils.print_curnode_lineage)
vim.keymap.set('t', '<ESC>', '<C-\\><C-n>')
vim.keymap.set('t', '<C-d>', terminal_to_buffer)

-- local current_node = vim.treesitter.get_node()
-- print(current_node:type())
-- print(current_node:parent())
-- types = {'dot_index_expression'}
-- print(vim.tbl_contains(types, current_node:type()))
-- print(current_node)

-- a = require('treesitter_utils')
-- print(a)
-- print(type(a))
-- print(a.find_node_ancestor)
-- print(a.find_node_ancestor({ 'chunk' }, current_node))

-- local chunk_node = require('treesitter_utils').M.find_node_ancestor({ 'chunk' }, current_node)
-- local chunk_node = M.find_node_ancestor({ 'chunk' }, current_node)


-- print(chunk_node:type())

-- lazy
require('config.lazy')
]]--
