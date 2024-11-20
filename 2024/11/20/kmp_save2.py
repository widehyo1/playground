from typing import List

bk = breakpoint

def make_pi_array(search_word: str) -> List[int]:
    print(f'=== make_pi_array({search_word}) ===')
    n = len(search_word)
    if n == 0:
        return []
    pi_array = [0] * n
    main_walker = 1
    sub_walker = 0
    pivot = 1

    while main_walker < n:
        if search_word[sub_walker] == search_word[main_walker]:
            sub_walker += 1
            pi_array[main_walker] = sub_walker
            main_walker += 1
        else:
            cur_sentence = search_word[pivot:main_walker + 1]
            cur_search_word = search_word[:sub_walker]
            print(f'{cur_sentence=}')
            print(f'{cur_search_word=}')
            print(f'{main_walker=}')
            print(f'{sub_walker=}')
            print(f'{pivot=}')
            print(f'{pi_array[:sub_walker]=}')
            # situation is the same as kmp when
            # search_word is found in sentence
            # we have pi_array of cur_search_word
            pivot = main_walker - pi_array[sub_walker - 1]
            sub_walker = pi_array[sub_walker - 1]
            if sub_walker == 0:
                pi_array[main_walker] = 0
                main_walker += 1
                pivot = main_walker

    return pi_array

def kmp(sentence: str, search_word: str) -> List[int]:
    n = len(sentence)
    m = len(search_word)
    index_list = []
    pi_array = make_pi_array(search_word)
    main_walker = 1
    sub_walker = 0
    while main_walker < n - m:
        if sentence[main_walker] == search_word[sub_walker]:
            main_walker += 1
            sub_walker += 1
            if sub_walker == m:
                index_list.append(main_walker - sub_walker)
                sub_walker = pi_array[sub_walker - 1]
        else:
            main_walker -= pi_array[sub_walker - 1]
    return index_list

if __name__ == '__main__':
    # search_word = 'aabaaaabaaabaababaaababaaaabaab'
    # search_word = 'aabaaaabaaabaab'
    # pi_array = make_pi_array(search_word)
    # print('result:')
    # print(pi_array)

    search_word = 'tomato'
    sentence = 'tomatitomatomato'
    index_list = kmp(sentence, search_word)
    print('result:')
    print(index_list)
