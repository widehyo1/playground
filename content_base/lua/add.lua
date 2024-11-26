-- add all elements of array a
function add (a)
    local sum = 0
    for i,v in ipairs(a) do
        sum = sum + v
    end
    return sum
end

s, e = string.find("hello Lua users", "Lua")
print(s, e)

function maximum (a)
    local mi = 1
    local m = a[mi]
    for i,val in ipairs(a) do
        if val > m then
            mi = i
            m = val
        end
    end
    return m, mi
end

print(maximum({8,10,23,12,5}))

f = string.find
a = {'hello', 'll'}

f(unpack(a))
