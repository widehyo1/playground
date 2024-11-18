from pprint import pprint

def make_pi_array(string):
    print(f'=== make_pi_array({string}) ===')
    n = len(string)
    pi_array = [0] * n
    idx = 0
    while idx < n - 1:
        walker_idx = 0
        counter = 0
        idx += 1
        print(f'{idx=}, {walker_idx=}, {counter=}')
        print(f'{string[walker_idx]=}, {string[idx]=}')
        if string[walker_idx] != string[idx]:
            pi_array[walker_idx] = counter
            continue
        else:
            while idx < n and string[walker_idx] == string[idx] :
                print(f'{idx=}, {walker_idx=}, {counter=}')
                print(f'{string[walker_idx]=}, {string[idx]=}')
                walker_idx += 1
                idx += 1
                counter += 1
                pi_array[idx-1] = counter
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

