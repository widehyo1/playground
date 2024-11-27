a = 'asdf'
b = 'qw'

function iterator (tbl, val)
    val = val or 1
    print(val)
    print(tbl[1])
    print(tbl[2])
    if string.len(tbl[1]) >= val and string.len(tbl[2]) >= val then
        return val + 1, string.sub(tbl[1], val, val), string.sub(tbl[2], val, val)
    elseif string.len(tbl[1]) >= val then
        -- tbl[1] is remains
        return val + 1, string.sub(tbl[1], val, val), 0
    elseif string.len(tbl[2]) >= val then
        return val + 1, string.sub(tbl[2], val, val), 1
    else
        return nil
    end
end

function zip_longest(it_a, it_b)
    local tbl = {it_a, it_b}
    local val = 1
    while val do
        return iterator, tbl, val
    end
end

for i, item_a, item_b in zip_longest(a, b) do
    print(i, item_a, item_b)
end
