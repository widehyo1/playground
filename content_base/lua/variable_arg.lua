printResult = ''

function print (...)
    for i,v in ipairs(arg) do
        printResult = printResult .. tostring(v) .. '\t'
    end
    printResult = printResult .. '\n'
end

local _, x = string.find(x, p)

print(string.find('hello hello', ' hel'))
print(select(1, string.find('hello hello', ' hel'))
print(select(2, string.find('hello hello', ' hel'))

function g (a, b, ...) end
