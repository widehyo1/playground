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


if __name__ == '__main__':
    string = [
          'ABCDABD'
        , 'ABACABABC'
        , 'ABACABABA'
        , 'PARTICIPATEINPARACHUTE'
    ]

    for _str in string:
        pi_array = make_pi_array(_str)
        pprint(pi_array)
        print()

