n, k = map(int, input().strip().split())
words = [input().strip() for _ in range(n)]

from typing import NamedTuple


def bit_representation(word, bit_position_dict):
    result = 0b0
    for char in word:
        result |= 0b1 << bit_position_dict[char]
    return result


def count_one_in_bit(bit, digit):
    return sum(1 for i in range(digit) if bit & (1 << i))


class Walker(NamedTuple):
    position_to_fill_zero: int
    remaining_zero_cnt: int
    bit_repr_tuple: tuple


def get_possible_word_num(n, k, words):
    chars = set()
    for word in words:
        chars |= set(word)

    bit_position_dict = {char: idx for idx, char in enumerate(list(chars))}
    distinct_char_num = len(bit_position_dict)

    if k >= distinct_char_num:
        return n

    bit_repr_list = [bit_representation(word, bit_position_dict) for word in words]

    mininum_distinct_char_cnt_to_complete_word = min(
        count_one_in_bit(bit_repr, distinct_char_num) for bit_repr in bit_repr_list
    )

    if k < mininum_distinct_char_cnt_to_complete_word:
        return 0
    remaining_zero_cnt = distinct_char_num - k

    cache = {}
    maximum_possible_cmp_word_cnt = 0

    position_to_fill_zero = 0
    bit_repr_tuple = tuple(bit_repr_list)
    walker = Walker(position_to_fill_zero, remaining_zero_cnt, bit_repr_tuple)

    def backtrack(walker: Walker):
        nonlocal cache, maximum_possible_cmp_word_cnt, distinct_char_num
        if walker in cache:
            return cache[walker]

        position_to_fill_zero, remaining_zero_cnt, bit_repr_tuple = walker
        current_result = len(bit_repr_tuple)

        if current_result < maximum_possible_cmp_word_cnt:
            # yields no result
            cache[walker] = None
            return cache[walker]

        if remaining_zero_cnt == 0:
            maximum_possible_cmp_word_cnt = max(
                current_result, maximum_possible_cmp_word_cnt
            )
            cache[walker] = current_result
            return cache[walker]

        if position_to_fill_zero + remaining_zero_cnt >= distinct_char_num:
            cache[walker] = None
            return cache[walker]

        backtrack(
            Walker(
                position_to_fill_zero + 1,
                remaining_zero_cnt - 1,
                filter_bit_repr(position_to_fill_zero + 1, bit_repr_tuple),
            )
        )
        # skip this position
        backtrack(Walker(position_to_fill_zero + 1, remaining_zero_cnt, bit_repr_tuple))

    def filter_bit_repr(position_to_fill_zero, bit_repr_tuple):
        nonlocal distinct_char_num
        return tuple(
            bit_repr
            for bit_repr in bit_repr_tuple
            if bit_repr & (1 << (distinct_char_num - 1 - position_to_fill_zero) == 0)
        )

    backtrack(walker)
    return maximum_possible_cmp_word_cnt


print(get_possible_word_num(n, k, words))
