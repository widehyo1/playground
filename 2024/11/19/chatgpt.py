from typing import List

bk = breakpoint  # Just for debugging purposes

def print_search_word(search_word, main_walker, sub_walker):
    print(''.join(gen_search_word_repr(search_word, main_walker, sub_walker)))

def print_pivot_search_word(search_word, pivot):
    print(''.join(gen_pivot_search_word(search_word, pivot)))

def gen_search_word_repr(search_word, main_walker, sub_walker):
    yield from ['v' if idx == main_walker else ' ' for idx in range(len(search_word))]
    yield '\n'
    yield from search_word
    yield '\n'
    yield from ['^' if idx == sub_walker else ' ' for idx in range(len(search_word))]

def gen_pivot_search_word(search_word, pivot):
    yield from search_word[:pivot]
    yield '['
    yield from search_word[pivot]
    yield ']'
    yield from search_word[pivot + 1:]

def print_current_step(search_word, main_walker, sub_walker, pivot):
    if pivot >= len(search_word):
        return
    print_search_word(search_word, main_walker, sub_walker)
    print_pivot_search_word(search_word, pivot)

def make_pi_array(search_word: str) -> List[int]:
    n = len(search_word)
    if n == 0:
        return []

    pi_array = [0] * n
    main_walker = 1  # Start from index 1
    sub_walker = 0  # Initially, no prefix matches
    counter = 0

    while main_walker < n:
        print_current_step(search_word, main_walker, sub_walker, counter)

        # Case 1: When characters match
        if search_word[sub_walker] == search_word[main_walker]:
            sub_walker += 1
            pi_array[main_walker] = sub_walker
            main_walker += 1
        else:
            # Case 2: When characters don't match, use pi array to skip
            if sub_walker > 0:
                sub_walker = pi_array[sub_walker - 1]
            else:
                pi_array[main_walker] = 0
                main_walker += 1
        
        print(f'{pi_array=}')
    return pi_array

if __name__ == '__main__':
    search_word = 'aabaaaabaaabaababaaabaabaaaabab'
    pi_array = make_pi_array(search_word)
    print(f'{pi_array=}')
