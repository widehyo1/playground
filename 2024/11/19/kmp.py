from typing import List

bk = breakpoint

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
    main_walker = 1
    sub_walker = 0
    pivot = 1
    while main_walker < n:
        print_current_step(search_word, main_walker, sub_walker, pivot)
        if search_word[sub_walker] == search_word[main_walker]:
            sub_walker += 1
            pi_array[main_walker] = sub_walker
            main_walker += 1
        else:
            if sub_walker > 0:
                sub_walker = pi_array[sub_walker - 1]
            else:
                pi_array[main_walker] = 0
                main_walker += 1
        print(f'{pi_array=}')
    return pi_array

def kmp(sentence, search_word):
    n = len(sentence)
    m = len(search_word)
    pi_array = make_pi_array(search_word)
    print(pi_array)
    found_indices = []
    main_walker = 0
    sub_walker = 0
    while main_walker <= n - m:
        if sentence[main_walker] != search_word[sub_walker]:
            main_walker += 1
        else:
            while main_walker < n and sentence[main_walker] == search_word[sub_walker]:
                main_walker += 1
                sub_walker += 1
                if sub_walker == m:
                    found_indices.append(main_walker - sub_walker)
                    break
            main_walker -= pi_array[sub_walker - 1]
            sub_walker = 0
    print(found_indices)
    return found_indices

if __name__ == '__main__':

    sentence = "ababbabaabbaabbabababaaaabbaaabaaabaaaabaaabaababaaabaabaaaababbbbabbbabaaaabbaaababbabaaaababbbbaabbaaabbbbbbaabbbababbabababaaaabbbabababaaaabbbabaaaabbbabbbbbabbbbaababbbababbaaabababaaaabbaabbabbbabbbbbabbaaababbbbabbaabaaaababbaababbabbbbbaaaabbaababbbabbbbbabababbbbaababbaabbbbbababbbbbbbbabab"
    search_word = 'aabaaaabaaabaababaaabaabaaaabab'

    m = len(search_word)
    for found_index in kmp(sentence, search_word):
        print(found_index)
        print(sentence[found_index:found_index + m])
