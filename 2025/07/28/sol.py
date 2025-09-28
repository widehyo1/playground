def sol(word):
    """
    abab -> ababa (5)
    abacaba -> abacaba (7)
    qwerty -> qwertytrewq (11)

    len(word) => at most 2 * len(word) + 1

    언제 이러지 않아도 되나

    한 문자씩 검사하면서 양쪽 끝으로 확장하여 sub palindrome 길이의 최대값을 구하자
    남은 길이를 더하면 된다.

    한번 문자를 보는데 O(n)
    확장하는데 O(n)
    O(n^2)

    근데, 짝수인 경우는?
    abba

    aabba
    
    한 문자씩이 아니겠네
    이 경우 연속적인 문자를 발견할 경우 사이를 기준으로 확장시켜야 함

    그리고 문자열은 항상 뒤에 추가함

    앞에 추가하지 못한다

    edcbbcdef
    fedcbbcdef <- 불가

    edcbbcdef

    문자의 끝을 포함해야만 하네
    앞만 남겨야되는구나
    true false flag 배열 생각 + false(not used)의 개수를 추가하면 됨

    뒤부터 찾아야겠는데?
    """
    n = len(word)
    if n == 0:
        return 0

    chars_to_add = [False] * n

    center = n - 1
    while center >= n // 2:
        target = word[center:][::-1]
        m = len(target)
        # 
        # center ~ m 반경 # 홀수일 때
        # 반경 1
        # 반경 2
        # abab
        #  ^^^
        # center = 2
        # m = 2
        # center - (m - 1) = 1

        # abba
        # ba: 반경 2 # 짝수일 때
        # ccabba
        # m = 2
        # center = 4

        if word[center - m + 1:center + 1] == target: # 홀수일 때
            print(f"flag1, {word[center - m + 1:center + 1]=}, {target=}")
            for idx in range(center - m + 1, n):
                chars_to_add[idx] = True
            print(f"{chars_to_add=}")
        if word[center-m:center] == target: # 짝수일 때
            print(f"flag2")
            for idx in range(center - m, n):
                chars_to_add[idx] = True
            print(f"{chars_to_add=}")
        center -= 1
    print(f"{chars_to_add=}")

    unpair_cnt = sum(1 for flag in chars_to_add if not flag)
    return n + unpair_cnt

word = input()
print(sol(word))
