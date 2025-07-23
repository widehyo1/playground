from typing import NamedTuple

class Walker(NamedTuple):
    idx: int
    zero_to_fill: int
    possible_reprs: tuple

def count_of_one(bit_repr):
    return sum(1 for bit in str(bin(bit_repr))[2:] if bit == '1')

def fill_zero(idx, possible_reprs):
    return tuple(
        possible_repr for possible_repr in possible_reprs
        if possible_repr & (1 << idx) == 0
    )

def sol(n, k, words):
    char_set = set()
    char_to_idx_dict = {}
    char_cnt = 0
    bit_reprs = []
    for word in words:
        bit_repr = 0b0
        for char in word:
            if char in char_set:
                bit_repr |= 1 << char_to_idx_dict[char]
                continue
            char_set.add(char)
            char_to_idx_dict[char] = char_cnt
            char_cnt += 1
            bit_repr |= 1 << char_to_idx_dict[char]
        bit_reprs.append(bit_repr)

    if char_cnt <= k:
        return n

    num_of_ones = [count_of_one(bit_repr) for bit_repr in bit_reprs]

    if k < min(num_of_ones):
        return 0

    possible_word_cnt = 0

    idx = 0
    zero_to_fill = char_cnt - k
    possible_reprs = tuple(bit_reprs)

    walker = Walker(idx, zero_to_fill, possible_reprs)

    def backtrack(walker: Walker):
        nonlocal char_cnt, possible_word_cnt

        idx, zero_to_fill, possible_reprs = walker
        # exit condition
        if zero_to_fill == 0:
            possible_word_cnt = max(possible_word_cnt, len(possible_reprs))
            return possible_word_cnt
        # base case1: no more room to fill zero
        if idx == char_cnt:
            return None
        # base case2: can not update result
        if len(possible_reprs) <= possible_word_cnt:
            return None
        # base case3: can not use remaining zeroes
        if zero_to_fill + idx >= char_cnt:
            return None

        # biz logic
        # try to fill zero
        backtrack(Walker(idx + 1, zero_to_fill - 1, fill_zero(idx, possible_reprs)))
        # skip this index
        backtrack(Walker(idx + 1, zero_to_fill, possible_reprs))

    backtrack(walker)
    return possible_word_cnt

n, k = map(int, input().split())
words = [input() for _ in range(n)]
result = sol(n, k, words)
print(result)
