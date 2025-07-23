from itertools import combinations

def sol(n, k, words):
    # 1. Construct distinct character set
    char_set = set()
    char_to_idx = {}
    char_cnt = 0
    bit_reprs = []

    # 2. Create bit representation of each word
    for word in words:
        bit_repr = 0b0
        for char in word:
            if char not in char_set:
                char_set.add(char)
                char_to_idx[char] = char_cnt
                char_cnt += 1
            bit_repr |= 1 << char_to_idx[char]
        bit_reprs.append(bit_repr)

    # If the number of distinct characters is less than or equal to k, all words are possible
    if char_cnt <= k:
        return n

    # 3. Base case: if it's impossible to form a word with the remaining available zeros
    num_of_ones = [bin(bit_repr).count('1') for bit_repr in bit_reprs]
    if k < min(num_of_ones):
        return 0

    # 4. Generate all possible positions to place zeros (k positions)
    possible_word_cnt = 0
    zero_positions = list(range(char_cnt))  # Indexes of positions we can fill zeros
    
    # Generate all combinations of positions to fill zeros
    for zero_fill_indices in combinations(zero_positions, k):
        # Create a new bitmask set where we will "turn off" the selected positions
        new_reprs = []
        for bit_repr in bit_reprs:
            modified_repr = bit_repr
            for idx in zero_fill_indices:
                modified_repr &= ~(1 << idx)  # Set the idx-th bit to 0
            new_reprs.append(modified_repr)

        # Count how many words are still possible with this combination of zero positions
        possible_word_cnt = max(possible_word_cnt, len(new_reprs))

    return possible_word_cnt
