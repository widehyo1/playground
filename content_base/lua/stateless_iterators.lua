a = {'one', 'two', 'three'}
for i, v in ipairs(a) do
    print(i, v)
end

function iter (a, i)
    i = i + 1
    local v = a[i]
    if v then
        return i, v
    end
end

function ipairs (a)
    return iter, a, 0
end

function pairs (t)
    return next, t, nil
end

--[[

The pairs function, which iterates over all elements in a table, is similar, except that the iterator function is the next function, which is a primitive function in Lua:

The call next(t, k), where k is a key of the table t, returns a next key in the table, in an arbitrary order. (It returns also the value associated with that key, as a second return value.) The call next(t, nil) returns a first pair. When there are no more pairs, next returns nil.
]]--

for k, v in next, t do
    ...
end

for k, v in next, t, nil do
    ...
end

local iterator

function allwords ()
    local state = {line = io.read(), pos = 1}
    return iterator, state
end

function iterator (state)
    --[[
    this example code illustrates not introducing
    upvalues but make it in state as a table
    a table as a invariant state can possess
    all upvalues as can
    ]]--
    while state.line do
        -- search for next word
        local s, e = string.find(state.line, '%w+', state.pos)
        if s then
            -- update next position (after this word)
            state.pos = e + 1
            return string.sub(state.line, s, e)
        else
            state.line = io.read()
            state.pos = 1
        end
    end
    return nil
end

--[[
Whenever it is possible, you should try to write stateless iterators, those that keep all their state in the for variables. With them, you do not create new objects when you start a loop. If you cannot fit your iteration into that model, then you should try closures. Besides being more elegant, typically a closure is more efficient than an iterator using tables: First, it is cheaper to create a closure than a table; second, access to upvalues is faster than access to table fields. Later we will see yet another way to write iterators, with coroutines. This is the most powerful solution, but a little more expensive.
]]--


function allwords (f)
    for l in io.lines() do
        for w in string.gfind(l, '%w+') do
            f(w)
        end
    end
end

allwords(print)

local count = 0
allwords(function (w)
    if w == 'hello' then count = count + 1 end
end)
print(count)


local count = 0
for w in allwords() do
    if w == 'hello' then count = count + 1 end
end
print(count)
