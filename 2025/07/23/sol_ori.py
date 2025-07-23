import random
import string

from typing import NamedTuple

def generate_random_string(length):
    characters = string.ascii_letters
    return "".join(random.choice(characters).lower() for i in range(length))

class Walker(NamedTuple):
    idx: int
    zero_to_fill: int
    possible_reprs: tuple

def count_of_one(bit_repr):
    return sum(1 for bit in str(bin(bit_repr))[2:] if bit == '1')

def fill_zero(idx, possible_reprs):
    """
    for each possible_repr in possible_reprs:
    see possible_repr's binary representation.
    if idx'th digit is 1, remove it
        it means by filling zero at idx'th digit, word can not made
    """
    return tuple(
        possible_repr for possible_repr in possible_reprs
        if possible_repr & (1 << idx) == 0
    )

def sol(n, k, words):
    # 1. construct distinct char set
    # 2. make bit_repr for each word
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

    print(f"{n=}, {k=}, {char_cnt=}")
    # 3. check base case1: all words are possible
    if char_cnt <= k:
        print("all words are possible")
        return n

    num_of_ones = [count_of_one(bit_repr) for bit_repr in bit_reprs]
    print(f"{num_of_ones=}")

    # 4. check base case2: any word can not be made
    if k < min(num_of_ones):
        print("any word can not be made")
        return 0

    # 5. store associative array for debugging
    bin_arr = [bin(bit_repr) for bit_repr in bit_reprs]
    assoc = dict(zip(words, zip(bin_arr, num_of_ones)))

    print(char_to_idx_dict)
    print(assoc)
    for word, value in sorted(assoc.items(), key=lambda item: item[1][1]):
        bit_repr, num_of_one = value
        print(f"{word:20}, {num_of_one:<2}, {str(bit_repr)[2:]:>26}")


    # 6. consider each bit_repr as a bit string of length char_cnt
    #    character is 1:
    possible_word_cnt = 0

    idx = 0
    zero_to_fill = char_cnt - k
    possible_reprs = tuple(bit_reprs)

    walker = Walker(idx, zero_to_fill, possible_reprs)

    def backtrack(walker: Walker):
        nonlocal char_cnt, possible_word_cnt

        idx, zero_to_fill, possible_reprs = walker
        print(f"{idx=}, {zero_to_fill=}, {len(possible_reprs)=}")
        # exit condition
        if zero_to_fill == 0:
            print("exit condition")
            possible_word_cnt = max(possible_word_cnt, len(possible_reprs))
            print(f"{possible_word_cnt=}")
            return possible_word_cnt
        # base case1: no more room to fill zero
        if idx == char_cnt:
            print("base case1")
            return None
        # base case2: can not update result
        if len(possible_reprs) <= possible_word_cnt:
            print("base case2")
            print(f"{len(possible_reprs)=}, {possible_word_cnt=}")
            return None


        # biz logic
        # try to fill zero
        backtrack(Walker(idx + 1, zero_to_fill - 1, fill_zero(idx, possible_reprs)))
        # skip this index
        backtrack(Walker(idx + 1, zero_to_fill, possible_reprs))

    backtrack(walker)
    return possible_word_cnt

if __name__ == '__main__':
    n, k = map(int, input().split())
    words = [input() for _ in range(n)]

#     n = 20
    # k = 22
#     k = 23
#     words  = [generate_random_string(random.randint(10, 20)) for _ in range(20)]
    result = sol(n, k, words)
    print(result)
