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
    pivot = 1
    sub_walker = 0
    counter = 0
    is_pivot_catched_main_walker = True
    while main_walker < n:
        print_current_step(search_word, main_walker, sub_walker, pivot)
        if search_word[sub_walker] == search_word[main_walker]:
            sub_walker += 1
            counter += 1
        else:
            print('===')
            sub_walker = 0
            counter = 0
            exit_flag = False
            while True:
                pivot += 1
                print_current_step(search_word, main_walker, sub_walker, pivot)
                if pivot > main_walker:
                    counter = 0
                    break
                if search_word[pivot] != search_word[sub_walker]:
                    continue
                capture = pivot
                while search_word[capture] == search_word[sub_walker]:
                    capture += 1
                    sub_walker += 1
                    counter += 1
                    print_current_step(search_word, main_walker, sub_walker, pivot)
                    if capture > main_walker:
                        exit_flag = True
                        break
                if exit_flag:
                    break
                sub_walker = 0
                counter = 0
        pi_array[main_walker] = counter
        main_walker += 1
        print(f'{counter=}')
        print(f'{pi_array=}')
    return pi_array


if __name__ == '__main__':
    search_word = 'aabaaaabaaabaababaaabaabaaaabab'
    # search_word = 'aabaaaab'
    # search_word = 'aabaa'
    pi_array = make_pi_array(search_word)
    print(f'{pi_array=}')
