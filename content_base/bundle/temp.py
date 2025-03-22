def get_highlight_position(position):
    flag = 0
    prev = -1
    start = -1
    result = []
    for pos in position:
        print(pos)
        if flag:
            print('flag1')
            if pos - prev == 1:
                print('flag3')
                prev = pos
            else:
                print('flag4')
                flag = 0
                result.append([start, pos])
        else:
            print('flag2')
            start = pos
            prev = pos
            flag = 1
    if flag:
        result.append([start, position[-1]])
    return result

print(get_highlight_position([54, 55, 56, 57, 58, 59]))
