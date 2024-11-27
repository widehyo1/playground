--[[ a construction like
for val_1, ..., val_n in explist do block end

is equivalent to the following code:

do
    local _f, _s, _val = explist
    while true do
        local val_1, ..., val_n = _f(_s, _var)
        _var = var_1
        if _var == nil then break end
        block
    end
end


generic for keeps three values:
The iterator function(_f)
an invariant state(_s)
control variable(_val)


So, if our iterator function is f, the invariant state is s,
and the initial value for the control variable is a_0.
the control variable will loop over the values
a_1 = f(s, a_0), a_2 = f(s, a_1), and so on, until a_i is nil.

If the for has other variables, then simply get the extra values returned
by each call to f
--]]
