function factorial(num)
    if (num == 1) then
        return num
    end
    return num * factorial(num - 1)
end

print('=== App start ===')
num = 5
result = factorial(num)
print('result: ' .. result)
print('=== App end ===')
