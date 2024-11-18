from pprint import pprint

def make_pi_array(search_word):
    print(f'=== make_pi_array({search_word}) ===')
    n = len(search_word)
    pi_array = [0] * n
    counter = 0
    walker_idx = 0
    for idx in range(1, n):
        if search_word[idx] == search_word[walker_idx]:
            walker_idx += 1
            counter += 1
        else:
            walker_idx = 0
            counter = 0
        pi_array[idx] = counter
    return pi_array

def kmp(sentence, search_word):
    n = len(sentence)
    m = len(search_word)
    pi_array = make_pi_array(search_word)
    found_indices = []
    main_walker = 0
    sub_walker = 0
    while main_walker <= n - m:
        sub_walker
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
    # search_word = 'tomato'
    # sentence = 'tomatitomatomato'
    search_word = 'aaba'
    sentence = 'aabaacaadaabaaba'
    m = len(search_word)
    for found_index in kmp(sentence, search_word):
        print(found_index)
        print(sentence[found_index:found_index + m])

