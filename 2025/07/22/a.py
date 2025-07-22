import random
import string

from typing import NamedTuple


def generate_random_string(length):
    characters = string.ascii_letters
    return "".join(random.choice(characters).lower() for i in range(length))


def print_bitmap(bitmap, digit):
    print("=== print bitmap ===")
    print("\n".join(str(bin(bit))[2:].zfill(digit) for bit in bitmap))


def transpose_bitmap(bitmap, distinct_char_num):
    transposed = []
    n = len(bitmap)
    for idx in reversed(range(distinct_char_num)):
        row_repr_num = 0b0
        for i, bit in enumerate(bitmap):
            row_repr_num |= ((bit & (1 << idx)) >> idx) << (n - 1 - i)
        transposed.append(row_repr_num)
    return transposed


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

    # init phase
    print_bitmap(bit_repr_list, distinct_char_num)
    t_bit_repr = transpose_bitmap(bit_repr_list, distinct_char_num)
    print_bitmap(t_bit_repr, n)

    # consider filling zeroes instead of filling ones
    remaining_zero_cnt = distinct_char_num - k
    print(f"{n=}")
    print(f"{distinct_char_num=}")
    print(f"{k=}")
    print(f"{remaining_zero_cnt=}")

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
            print("base condition1")
            return cache[walker]

        position_to_fill_zero, remaining_zero_cnt, bit_repr_tuple = walker

        current_result = len(bit_repr_tuple)

        # base case2: can not update maximum_possible_cmp_word_cnt
        if current_result < maximum_possible_cmp_word_cnt:
            print("base condition2")
            # yields no result
            cache[walker] = None
            return cache[walker]

        # base case3: spend all zeroes
        if remaining_zero_cnt == 0:
            print("base condition3")
            # update maximum_possible_cmp_word_cnt
            maximum_possible_cmp_word_cnt = max(
                current_result, maximum_possible_cmp_word_cnt
            )
            cache[walker] = current_result
            print(f"{current_result=}")
            return cache[walker]

        # base case4: can not use all zeroes
        if position_to_fill_zero + remaining_zero_cnt >= distinct_char_num:
            print("base condition4")
            # all position tried but remaining_zero_cnt > 0
            # yields no result
            cache[walker] = None
            return cache[walker]

        # biz logic

        print(
            f"{position_to_fill_zero=}, {remaining_zero_cnt=}, {len(bit_repr_tuple)=}"
        )
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
    print("=" * 100)
    print()
    print(f"{maximum_possible_cmp_word_cnt=}")
    return maximum_possible_cmp_word_cnt


if __name__ == "__main__":
    #     n = 20
    #     k = 17
    #     words  = [generate_random_string(random.randint(10, 20)) for _ in range(20)]
    n = 4
    k = 2
    words = [
        "ab",
        "ac",
        "bc",
        "abc",
    ]
    get_possible_word_num(n, k, words)
