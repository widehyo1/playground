-- located in /usr/local/share/lua/5.1/treesitter_utils.lua
-- define module to export
M = {}

function M.find_node_ancestor(types, node)
    if not node then
        return nil
    end

    if vim.tbl_contains(types, node:type()) then
        return node
    end

    local parent = node:parent()

    return M.find_node_ancestor(types, parent)
end

function M.get_node_lineage(node)
    result = {}
    idx = 1
    curnode = node
    while curnode do
        result[idx] = curnode
        curnode = curnode:parent()
        idx = idx + 1
    end
    return result
end


function M.print_curnode_lineage()
    local current_node = vim.treesitter.get_node()
    node_lineage = M.get_node_lineage(current_node)
    res = ''
    len = #node_lineage
    for k, v in ipairs(node_lineage) do
        res = res .. '(' .. (len - k) .. ')' .. v:type() .. ' '
    end
    print(res)
end

-- export module
return M
