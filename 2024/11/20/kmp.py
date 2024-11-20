from typing import List

bk = breakpoint

def print_main_sub_walker_word(word, main_walker, sub_walker):
    print(''.join(gen_main_sub_walker_word_repr(word, main_walker, sub_walker)))

def print_pivot_word(word, pivot):
    print(''.join(gen_pivot_word_repr(word, pivot)))

def gen_main_sub_walker_word_repr(word, main_walker, sub_walker):
    yield from ['=' for idx in range(len(word))]
    yield '\n'
    yield from ['v' if idx == main_walker else ' ' for idx in range(len(word))]
    yield '\n'
    yield from word
    yield '\n'
    yield from ['^' if idx == sub_walker else ' ' for idx in range(len(word))]

def gen_pivot_word_repr(search_word, pivot):
    yield from ['~' for idx in range(len(search_word))]
    yield '\n'
    yield from search_word[:pivot]
    yield '['
    yield from search_word[pivot]
    yield ']'
    yield from search_word[pivot + 1:]

def gen_walker_word_repr(word, walker):
    yield from ['v' if idx == walker else ' ' for idx in range(len(word))]
    yield '\n'
    yield from word

def print_walker_word(word, walker):
    print(''.join(gen_walker_word_repr(word, walker)))

def print_current_step(search_word, main_walker, sub_walker, pivot, show_pivot):
    if pivot >= len(search_word):
        return
    if show_pivot:
        print_pivot_word(search_word, pivot)
    print_main_sub_walker_word(search_word, main_walker, sub_walker)

def print_kmp_current_step(sentence, main_walker, search_word, sub_walker, main_pivot, sub_pivot, show_main_pivot, show_sub_pivot):
    print('-' * 40)
    if show_main_pivot:
        print_pivot_word(sentence, main_pivot)
    print('sentence:')
    print_walker_word(sentence, main_walker)
    if show_sub_pivot:
        print_pivot_word(search_word, sub_pivot)
    print('search_word:')
    print_walker_word(search_word, sub_walker)


def make_pi_array(search_word: str) -> List[int]:
    n = len(search_word)
    if n == 0:
        return []
    pi_array = [0] * n
    main_walker = 1
    sub_walker = 0
    pivot = 1
    show_pivot = True

    while main_walker < n:
        print_current_step(search_word, main_walker, sub_walker, pivot, show_pivot)
        if search_word[sub_walker] == search_word[main_walker]:
            show_pivot = False
            sub_walker += 1
            pi_array[main_walker] = sub_walker
            main_walker += 1
        else:
            show_pivot = True
            cur_sentence = search_word[pivot:main_walker + 1]
            cur_search_word = search_word[:sub_walker]
            if sub_walker > 0:
                print(f'*** mismatch ***')
                print(f'{cur_sentence=}')
                print(f'{cur_search_word=}')
            # situation is the same as kmp when
            # search_word is found in sentence
            # we have pi_array of cur_search_word
            pivot = main_walker - pi_array[sub_walker - 1]
            sub_walker = pi_array[sub_walker - 1]
            if sub_walker == 0:
                pi_array[main_walker] = 0
                main_walker += 1
                pivot = main_walker

    cur_sentence = search_word[pivot:main_walker + 1]
    cur_search_word = search_word[:sub_walker]
    print(f'{cur_sentence=}')
    print(f'{cur_search_word=}')

    print(f'result pi_array of {search_word}:')
    print(pi_array)
    return pi_array

def kmp(sentence: str, search_word: str) -> List[int]:
    n = len(sentence)
    m = len(search_word)
    index_list = []
    pi_array = make_pi_array(search_word)
    main_walker = 0
    sub_walker = 0
    main_pivot = 0
    sub_pivot = 0
    show_main_pivot = True
    show_sub_pivot = False
    while main_walker <= n - m:
        print_kmp_current_step(sentence, main_walker, search_word, sub_walker, main_pivot, sub_pivot, show_main_pivot, show_sub_pivot)
        if sentence[main_walker] != search_word[sub_walker]:
            main_walker += 1
            main_pivot = main_walker
            show_main_pivot = True
        else:
            show_main_pivot = False
            sub_pivot = sub_walker
            while main_walker < n and sentence[main_walker] == search_word[sub_walker]:
                show_sub_pivot = False
                main_walker += 1
                sub_walker += 1
                print_kmp_current_step(sentence, main_walker, search_word, sub_walker, main_pivot, sub_pivot, show_main_pivot, show_sub_pivot)
                if sub_walker == m:
                    index_list.append(main_walker - sub_walker)
                    break
            main_walker -= pi_array[sub_walker - 1]
            main_pivot = main_walker
            sub_walker = 0
            sub_pivot = sub_walker
            show_sub_pivot = False
    return index_list

if __name__ == '__main__':
    # search_word = 'aabaaaabaaabaababaaababaaaabaab'
    # search_word = 'aabaaaabaaabaab'
    # pi_array = make_pi_array(search_word)
    # print('result:')
    # print(pi_array)

    # search_word = 'tomato'
    # sentence = 'tomatitomatomato'
    # pi_array = make_pi_array(search_word)
    # index_list = kmp(sentence, search_word)
    # print('result:')
    # print(index_list)
    # m = len(search_word)
    # for idx in index_list:
    #     print(idx)
    #     print(sentence[idx:idx + m])


    samples = [('tomato' ,'tomatitomatomato'), ('aaba' ,'aabaacaadaabaaba'), ("abab" ,"abababab"), ("aaaa" ,"aaaaaa"), ("aabaaac" ,"aabaaabaaac"),]
    for search_word, sentence in samples:
        # make_pi_array(search_word)
        index_list = kmp(sentence, search_word)
        break

