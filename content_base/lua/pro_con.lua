function producer ()
    while true do
        local x = io.read()
        send(x)
    end
end

function consumer ()
    while true do
        local x = receive()
        io.write(x, '\n')
    end
end

function receive ()
    local status, value = coroutine.resume(producer)
    return value
end

function send (x)
    coroutine.yield(x)
end

producer = coroutine.create(
    function ()
        while true do
            local x = io.read()
            send(x)
        end
    end)

function recieve (prod)
    local status, value = coroutine.resume(prod)
    return value
end

function send (x)
    coroutine.yield(x)
end

function producer ()
    return coroutine.create(function ()
        while true do
            local x = io.read()
            send(x)
        end
    end)
end

function filter (prod)
    return coroutine.create(function ()
        local line = 1
        while true do
            local x = recieve(prod)
            x = string.format('%5d %s', line, x)
            send(x)
            line = line + 1
        end
    end)
end

function consumer (prod)
    while true do
        local x = recieve(prod)
        io.write(x, '\n')
    end
end

p = producer()
f = filter(p)
consumer(f)

consumer(filter(producer()))
