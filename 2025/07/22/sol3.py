from typing import NamedTuple


def bit_representation(word, bit_position_dict):
    """
    bit_position_dict consist of (character, position) pair, position represents
    binary number's digit that corresponding character.

    inspect each character in word
    1) extract position of character by bit_position_dict[character]
    2) let binary numbers position to be one (by bit operation "or")

    after all character inspected, the result is the binary representation of the word
    """
    result = 0b0
    for char in word:
        result |= 0b1 << bit_position_dict[char]
    return result


def count_one_in_bit(bit, digit):
    """
    if i'th binary digit is one, add one
    apply it
    """
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

    # base case1: all words can be constructed
    if k >= distinct_char_num:
        return n

    bit_repr_list = [bit_representation(word, bit_position_dict) for word in words]

    # base case2: any word can not be constructed
    mininum_distinct_char_cnt_to_complete_word = min(
        count_one_in_bit(bit_repr, distinct_char_num) for bit_repr in bit_repr_list
    )

    if k < mininum_distinct_char_cnt_to_complete_word:
        return 0

    ## biz logic

    # consider filling zeroes instead of filling ones
    remaining_zero_cnt = distinct_char_num - k

    # walk from distinct_char_num'th digit to 0 digit tracked by variable position
    # whenever fill zero at the position:
    #     decrease remaining_zero_cnt
    #         if remaining_zero_cnt is less than zero, break
    #     discard word_representation such that position'th number is one from bit_repr_list
    #     it means we decided to not choose that charcter, so that there is no possibility to complete that word_representation
    # to prune possiblity, track the variable maximum_possible_cmp_word_cnt, within this scope
    # if len(bit_repr_list) is less than maximum_possible_cmp_word_cnt, do not step forward
    #     it means, there is no possibility to update maximum_possible_cmp_word_cnt
    # after using all zeros, the length of bit_repr_list, denoted current_result, is compared to maximum_possible_cmp_word_cnt
    # if current_result > maximum_possible_cmp_word_cnt:
    #     maximum_possible_cmp_word_cnt = current_result

    cache = {}
    maximum_possible_cmp_word_cnt = 0

    position_to_fill_zero = 0
    bit_repr_tuple = tuple(bit_repr_list)
    walker = Walker(position_to_fill_zero, remaining_zero_cnt, bit_repr_tuple)

    def backtrack(walker: Walker):
        nonlocal cache, maximum_possible_cmp_word_cnt, distinct_char_num
        # base case1: cached
        if walker in cache:
            return cache[walker]

        position_to_fill_zero, remaining_zero_cnt, bit_repr_tuple = walker

        current_result = len(bit_repr_tuple)

        # base case2: can not update maximum_possible_cmp_word_cnt
        if current_result < maximum_possible_cmp_word_cnt:
            # yields no result
            cache[walker] = None
            return cache[walker]

        # base case3: spend all zeroes
        if remaining_zero_cnt == 0:
            # update maximum_possible_cmp_word_cnt
            maximum_possible_cmp_word_cnt = max(
                current_result, maximum_possible_cmp_word_cnt
            )
            cache[walker] = current_result
            return cache[walker]

        # base case4: can not use all zeroes
        if position_to_fill_zero + remaining_zero_cnt >= distinct_char_num:
            # all position tried but remaining_zero_cnt > 0
            # yields no result
            cache[walker] = None
            return cache[walker]

        # biz logic
        # fill zero
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
            if bit_repr & (1 << (distinct_char_num - 1 - position_to_fill_zero)) == 0
        )

    backtrack(walker)
    return maximum_possible_cmp_word_cnt


n, k = map(int, input().strip().split())
words = [input().strip() for _ in range(n)]

print(get_possible_word_num(n, k, words))
