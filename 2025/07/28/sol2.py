def findContentChildren(self, g: List[int], s: List[int]) -> int:
    # step1: sort
    g.sort()
    s.sort()

    child_cnt = len(g)
    cookie_cnt = len(s)

    # step2: two pointer
    pointer_g = 0
    pointer_s = 0

    content_child_cnt = 0

    while pointer_g < child_cnt and pointer_s < cookie_cnt:
        if g[pointer_g] <= s[pointer_s]:
            # give cookie to pointer_g th child
            content_child_cnt += 1
            pointer_g += 1
            pointer_s += 1
        else:
            # check next cookie
            pointer_s += 1

    return content_child_cnt

