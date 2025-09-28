from itertools import combinations
import sys

def count_distinct_char(word_repr):
    return sum(1 for idx in range(26) if word_repr & (1 << idx))

def sol(n, k, words):
    alpha_info = [False] * 26
    word_dict = {}
    for word in words:
        word_repr = 0
        for char in word:
            idx = ord(char) - ord('a')
            alpha_info[idx] = True
            word_repr |= 1 << idx
        word_dict[word] = word_repr

    if k >= sum(1 for alpha in alpha_info if alpha):
        return n
    if k < min(count_distinct_char(word_repr) for word_repr in word_dict.values()):
        return 0

    constructable_word_cnt = 0
    char_idxs = [idx for idx, alpha in enumerate(alpha_info) if alpha]
    word_repr_list = list(word_dict.values())

    # for idx, word_item in enumerate(word_dict.items()):
    #     word, word_repr = word_item
    #     word_repr_bin = bin(word_repr)
    #     print(f"{idx=}, {word=}, {word_repr_bin=}")

    for combination in combinations(char_idxs, k):
        print(combination)
        constructable_word_cnt_by_comb = 0

        comb_repr = 0
        for comb in combination:
            comb_repr |= 1 << comb

        for idx, word_repr in zip(reversed(range(n)), word_repr_list):
            remaining_constructable_word_cnt = idx + 1
            if remaining_constructable_word_cnt+ constructable_word_cnt_by_comb <= constructable_word_cnt:
                break
            if word_repr | comb_repr == comb_repr:
                constructable_word_cnt_by_comb += 1

        constructable_word_cnt = max(constructable_word_cnt_by_comb, constructable_word_cnt)
        print(constructable_word_cnt)

    return constructable_word_cnt

input = sys.stdin.readline
n, k = map(int, input().split())
words = [input().strip() for _ in range(n)]

print(sol(n, k, words))

