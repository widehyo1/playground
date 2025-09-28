def sol(word):
    n = len(word)
    if n == 0:
        return 0

    chars_to_add = [False] * n

    center = n - 1
    while center >= n // 2:
        target = word[center:][::-1]
        m = len(target)

        if word[center - m + 1:center + 1] == target: # 홀수일 때
            for idx in range(center - m + 1, n):
                chars_to_add[idx] = True
        if word[center-m:center] == target: # 짝수일 때
            for idx in range(center - m, n):
                chars_to_add[idx] = True
        center -= 1

    unpair_cnt = sum(1 for flag in chars_to_add if not flag)
    return n + unpair_cnt

word = input()
print(sol(word))
