co = coroutine.create(function ()
    print('hi')
end)

print(co)

print(coroutine.status(co))

coroutine.resume(co)

print(coroutine.status(co))

co = coroutine.create(function ()
    for i=1,10 do
        print('co', i)
        coroutine.yield()
    end
end)

coroutine.resume(co)

print(coroutine.status(co))

coroutine.resume(co)
coroutine.resume(co)
coroutine.resume(co)
coroutine.resume(co)
coroutine.resume(co)
coroutine.resume(co)
coroutine.resume(co)
coroutine.resume(co)
coroutine.resume(co)

print(coroutine.resume(co))
print(coroutine.resume(co))

co = coroutine.create(function (a,b,c)
    print('co', a, b, c)
end)

coroutine.resume(co, 1, 2, 3)

co = coroutine.create(function (a, b)
    coroutine.yield(a + b, a - b)
end)
print(coroutine.resume(co, 20, 10))

co = coroutine.create(function ()
    print('co', coroutine.yield())
end)

coroutine.resume(co)
coroutine.resume(co, 4, 5)

co = coroutine.create(function ()
    return 6, 7
end)
print(coroutine.resume(co))
