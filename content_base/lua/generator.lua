function gen_zip_string (str1, str2)
    local idx = 1
    local tbl = {str1, str2}
    while idx do
        return _gen_zip_string, tbl, idx
    end
end

function _gen_zip_string (tbl, idx)
    n = string.len(tbl[1])
    m = string.len(tbl[2])
    if idx <= n and idx <= m then
        return idx + 1, string.sub(tbl[1], idx, idx) .. string.sub(tbl[2], idx, idx)
    elseif idx <= n then
        return idx + 1, string.sub(tbl[1], idx, idx)
    elseif idx <= m then
        return idx + 1, string.sub(tbl[2], idx, idx)
    else
        return nil
    end
end

a = 'qwer'
b = 'asdfzxcv'

result = ''

-- for walker, value in gen_zip_string(a, b) do
for walker, value in gen_zip_string(b, a) do
    -- print(value)
    result = result .. value
end

print(result)
