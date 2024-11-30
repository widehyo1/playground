-- set leader key to comma
vim.g.mapleader = ','
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

treesitter_utils = require('treesitter_utils')

vim.keymap.set('n', '<leader>t', treesitter_utils.print_curnode_lineage)

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

