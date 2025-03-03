vim9script
# var i = 1
# while i < 5
#   echo "count is" i
#   i += 1
# endwhile
#
# for ii in range(1, 4)
#   echo "count is" ii
# endfor

# var counter = 0
# def g:GetCount(): number
#   s:counter += 1
#   return s:counter
# enddef
# echo g:GetCount()
# echo g:GetCount()

def Show(start: string, ...items: list<string>)
  echohl Title
  echo "start is " .. start
  echohl None
  for index in range(len(items))
    echon "  Arg " .. index .. " is " .. items[index]
  endfor
  echo
enddef

Show('Title', 'one', 'two', 'three')
