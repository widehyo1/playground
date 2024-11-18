from pprint import pprint

def make_pi_array(search_word):
    print(f'=== make_pi_array({search_word}) ===')
    n = len(search_word)
    pi_array = [0] * n
    walker_idx = 0
    for idx in range(1, n):
        while walker_idx > 0 and search_word[walker_idx] != search_word[idx]:
            walker_idx = pi_array[walker_idx-1]
        if search_word[walker_idx] == search_word[idx]:
            walker_idx += 1
            pi_array[idx] = walker_idx
    return pi_array

# [KMP 알고리즘(문자열 찾기)](https://cantcoding.tistory.com/13)
def makeTable(P):#P는 패턴
    lp=len(P) 
    Table=[0]*lp #패턴의 길이와 같은크기의 테이블 생성 
    i=0          #i를 사용하여 테이블 값을 갱신한다
    for j in range(1,lp):
        while i>0 and P[i]!=P[j]:  #i와 j가 다르면 i는 i-1의 테이블값 인덱스로 돌아간다
            i=Table[i-1]            #왜?->현재의 i에서 j와 다르니 i가 +1되었던것을 되돌아가서
                                    #i-1에서의 테이블값 인덱스에서 다시 j와 비교해준다
                                    #테이블에는 최대 공통 부분들이 있어서 돌아갈지점을 계속 갱신해주다가
                                    #0까지 가면 0이 된다.0을 저장하고 다음 j로 넘어간다
                                    
        if P[i]==P[j]:              #만약 같으면 i값을 1더해주고 table값에 넣는다.
            i+=1                    #i,j둘다 1씩 증가한다
            Table[j]=i
    return Table

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
    # search_word = 'tomato'
    # sentence = 'tomatitomatomato'

    # search_word = 'aaba'
    # sentence = 'aabaacaadaabaaba'

    # search_word = "abab"
    # sentence = "abababab"


    # search_word = "aaaa"
    # sentence = "aaaaaa"

    # sentence = "aabaaabaaac"
    # search_word = "aabaaac"

    sentence = "ababcaababcaabc"
    # search_word = "ababcaabc"
    search_word = "aabaabcaaabc"

    print(make_pi_array(search_word))
    # print(makeTable(search_word))
    # m = len(search_word)
    # for found_index in kmp(sentence, search_word):
    #     print(found_index)
    #     print(sentence[found_index:found_index + m])

