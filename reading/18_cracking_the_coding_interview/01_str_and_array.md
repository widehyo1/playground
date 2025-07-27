01_01_01. 중복이 없는가: 문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘을
작성하라. 자료구조를 추가로 사용하지 않고 풀 수 있는 알고리즘 또한 고민하라.

```whiteboard
가장 먼저 생각할 수 있는 건 set을 이용하는 방법이네요.
set chars를 선언하고 in 주어진 문자열의 문자를 하나씩 읽으며 set에 있는지 판단하고
있다면 True를 반환하면 되겠어요.

가장 쉽게는 return len(set(sentence)) == len(sentence) 을 하면 되겠어요.


```

```py
def check_string_has_duplicate_char(sentence: str):
    return len(set(sentence)) == len(sentence)
```

01_01_02. 순열확인: 문자열 두 개가 주어졌을 때 이 둘이 서로 순열 관계에 있는지 확인하는 메서드를 작성하라.
```whiteboard
일단 두개의 파라미터 sentence1, sentence2 (이하 st1, st2)를 매개변수로 받아야겠네요.

서로 순열 관계에 있다는 것은 문자구성이 같다는 이야기니, st1의 문자구성과 st2의 문자구성이 같은지 확인할게요.

st1이 aaabbc 라면 a:3, b:2, c:1 이고 st2가 bacaba 라면 a:3, b:2, c:1이니, 서로 순열관계에 있네요.
이를 확인하는 코드는 새로운 문자를 발견할 때마다 해당 문자의 카운터를 늘리면 됩니다.

최소한 두 문자열을 한번씩은 읽어야 하니, 최소 시간 복잡도는 O(n + m), n = len(st1), m = len(st2)이고
최소 공간복잡도는 역시 n + m 이네요.

생각한 알고리즘은 시간복잡도가 O(n + m)이고 공간복잡도 또한 2s, s = max(len(st1) + len(st2)) 이니, 작성해도
될 것 같습니다.
```

```py
def has_equivalent_permutation(st1: str, st2: str):
    char_counter1, char_counter2 = dict(), dict()
    for char in st1:
        char_counter1[char] = char_counter1.get(char, 0) + 1
    for char in st2:
        char_counter2[char] = char_counter2.get(char, 0) + 1
    if len(char_counter1) != len(char_counter2):
        return False
    for key in char_counter1.keys():
        if char_counter2.get(key, None) is None:
            return False
        if char_counter1[key] != char_counter2[key]:
            return False
    return True
```

01_01_03. URL화: 문자열에 들어 있는 모든 공백을 '%20'으로 바꿔 주는 메서드를 작성하라.
최종적으로  문자를 다 담을 수 있을 만큼 충분한 공간이 이미
확보되어 있으며 문자열의 최종 길이가 함께 주어진다고 가정해도 된다(자바로 구현한다면 배열 안에서 작업할 수 있도록 문자 배열(character array)을
이용하기 바란다).
예제:
입력: "Mr John Smith", 13
출력: "Mr%20John%20Smith"

```whiteboard
가장 nice한 풀이는 정규표현식을 이용하는 방법이겠네요. 하지만 저는 정규표현식 문법을 다
외우고 있지 않아서 한 문자씩 검사하는 로직을 사용하겠습니다. 컴퓨터 환경이었으면 python
실행하고 import re; help(re)로 원하는 메서드 찾아서 사용할 거예요.

한 문자씩 검사하고 해당 글자를 바꾸는 로직이니, apply helper function을 이용하는게
좋아보입니다. 문자열을 문자의 list로 바꾸고, 각 원소를 검사해서 " "과 같으면 "%20"으로
전환하는 apply function을 적용시켜 새로운 문자 리스트를 만든다음 join함수를 이용해
풀겠습니다.

이게 가능한 이유는 문자배열을 사용할 수 있고, 해당하는 길이가 주어졌으니 array로도 바로
적용할 수 있겠어요.

잠시만요, 문자의 공백이라는 건 " "만 의미합니까, whitespace 줄바꿈, 탭 등을 모두
의미합니까?

```

```py

def space_url_encode(text: str, size: int):
    char_arr = [''] * size
    for idx, char in enumerate(text):
        char_arr[idx] = char
    # 혹은 split 사용
    # char_arr = text.split('')

    space_converter = lambda char: "%20" if char == " " else char

    print(''.join(apply(char_arr, space_converter)))

def apply(arr: list[str], func: "Callable[str, str]"):
    for idx, item in enumerate(arr):
        arr[idx] = func(item)
    return arr

###
import re

def space_url_encode(text: str, size: int):
    print(re.sub(r" ", r"%20", text))
```


01_01_04 회문 순열: 주어진 문자열이 회문의 순열인지 아닌지 확인하는 함수를 작성하라.
회문이란 앞으로 읽으나 뒤로 읽으나 같은 단어 혹은 구절을 의미하며, 순열이란 문자열을
재배치하는 것을 뜻한다. 회문이 꼭 사전에 등장하는 단어로 제한될 필요는 없다.
예제
입력: Tact Coa
출력: True (순열: "taco cat", "atco cta" 등)

```whiteboard
먼저 예제에서 공백을 무시하고 lowercase만 따지는 것으로 보이는데 이렇게 가정하고 풀어도
괜찮은가요? 이렇게 진행하겠습니다. 먼저 전처리부터 해야겠네요. 공백을 탈락시키고 소문자로
만들게요. 다음은 trivial case 쳐내고 가겠습니다. len이 0이거나 1이면 true예요. 그리고
순열을 찾는 문제이기 때문에 주어진 입력의 문자구성만 관심대상입니다. 전처리된 문자가
홀수인 경우 문자당 등장수는 모두 짝수이거나, 단 하나만 홀수를 허용하고, 짝수인 경우는
문자당 등장수가 모두 짝수인지만 판단하면 됩니다. 전처리의 space 탈락에서 N, lowercase에서
N, 입력문자구성에서 한번만 문자를 읽으니 N이니 최소 시간 복잡도N을 만족합니다. 추가
공간복잡도도 counter 정보만 추가하니 여기도 N이니 풀이에 들어가도 되겠습니다.
```

```py
def is_palindrome_permutation(text: str) -> bool:
    # pre processing
    text = ''.join(text.split(' '))
    text = text.lower()
    n = len(text)
    char_info = {}
    for char in text:
        char_info[char] = char_info.get(char, 0) + 1
    if n % 2 == 0:
        for key in char_info.keys():
            if char_info[key] % 2 == 1:
                return False
    else:
        odd_flag = False
        for key in char_info.keys():
            if char_info[key] % 2 == 1:
                if odd_flag:
                    return False
                else:
                    odd_flag = True
    return True

```

01_01_05 하나 빼기: 문자열을 편집하는 방법에는 세 가지 종류가 있다. 문자 삽입, 문자 삭제,
문자 교체. 문자열 두 개가 주어졌을 때, 문자열을 같게 만들기 위한 편집 횟수가 1회 이내인지
확인하는 함수를 작성하라.
예제
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, blke -> flase

```whiteboard
일단 function signature는 문자열 두개를 인자로 받아 bool을 리턴하는 함수네요.
두가지 경우로 분기됩니다. 주어진 두 문자의 길이의 차가 0이거나 1인 경우만 True를 반환할 수
있어요. 아닌 경우 모두 False를 반환합니다.
두 문자의 길이의 차가 0이라면 단 한번의 문자교체만 이용하여 두 문자가 같아지는 경우입니다.
두 문자를 같이 순회하면서 처음으로 다른 문자를 찾으면 flag를 True로 설정하고 다른 문자를
찾았을 때 이미 flag가 Ture이면 False를 반환합니다. 아닌 경우엔 편집횟수 1회 이내로 만들수
있으니 True네요.
1이라면 처음으로 다른 문자를 찾아 그 index를 기록합니다. 두 문자열 중에서 길이가 더 큰
문자열 s에 대하여 s[:index] + s[index + 1:] == s2인지 확인하면 되겠네요.

이건 0인 경우에도 똑같이 적용할 수 있군요
```


```py
def is_edit_distance_less_than_one(txt1: str, txt2: str) -> bool:
    if txt1 == txt2:
        return True
    n1, n2 = len(txt1), len(txt2)
    if n1 - n2 > 1:
        return False
    if n1 == n2:
        diff_index = -1
        for idx in range(n1):
            if txt1[idx] != txt2[idx]:
                diff_index = idx
                break
        return discard_at_i(txt1, diff_index) == discard_at_i(txt2, diff_index)
    # abs(n1 - n2) == 1
    if n1 > n2:
        diff_index = -1
        for idx in range(n2):
            if txt1[idx] != txt2[idx]:
                diff_index = idx
                break
        else:
            diff_index = n2
        return discard_at_i(txt1, diff_index) == txt2
    if n1 < n2:
        diff_index = -1
        for idx in range(n1):
            if txt1[idx] != txt2[idx]:
                diff_index = idx
                break
        else:
            diff_index = n1
        return discard_at_i(txt2, diff_index) == txt1


def discard_at_i(txt: str, i: int) -> str:
    return txt[:i] + txt[i+1:]
```

01_01_06 문자열 압축: 반복되는 문자의 개수를 기본적인 문자열 압축 메서드를 작성하라. 예를
들어 문자열 aabccccaaa를 압축하면 a2b1c5a3이 된다. 만약 '압축된' 문자열의 길이가 기존
문자열의 길이보다 길다면 기존 문자열을 반환해야 한다. 문자열은 대소문자 알파벳(a~z)으로만
이루어져 있다.

```whiteboard
런랭스 인코딩 문제네요.
itertools의 group by를 사용하겠습니다.
```

```py
from itertools import groupby
def compress_by_rle(txt: str) -> txt:
    n = len(txt)
    rle_result = ''
    for groupper, iterator for groupby(txt):
        rle_result += f"{grouper}{len(iterator)}"
    if len(rle_result) > n:
        return txt
    return rle_result

```

01_01_07 행렬회전: 이미지를 표현하는 N * N 행렬이 있다. 이미지의 각 픽셀은 4바이트로
표현된다. 이때, 이미지를 90도 회전시키는 메서드를 작성하라. 행렬을 추가로 사용하지
않고서도 할 수 있겠는가?

```whiteboard
4byte는 어떤 형식인지는 모르겠지만 일단 int라고 하겠습니다.

ori
1 2
3 4
---
rotate to right
3 1
4 2
---
rotate to left
2 4
1 3


일단, 회전은 오른쪽으로 회전과 왼쪽으로 회전이 있네요.
행과 열이 바뀌므로, 행단위를 재배열 하는 방식으로 접근해 보겠습니다.

그보다 먼저 예시 하나만 더 볼게요

1 2 3
4 5 6
7 8 9
---
rotate to right
7 4 1
8 5 2
9 6 3
---
rotate to left
3 6 9
2 5 8
1 4 7

[
    [1 2 3]
    [4 5 6]
    [7 8 9]
]

오른쪽 회전의 경우
각 행내의 순서는 유지되지만, 행번호는 반대로
^
1
2
3
v

왼쪽 회전의 경우
각 행번호는 유지되지만, 행내 순서는 반대로
^
3
2
1
v

오른쪽 회전

열 정보 획인
[
    [7 8 9]
    [4 5 6]
    [1 2 3]
]
이걸 행렬 바꾸면 된다

행렬 바꾸는건 아래에도 쓸거니까 모듈화

파이썬 이용해서 첫번째 배열의 크기를 보고
zip하면 어떨까? 배열의 크기만큼 하기 힘들긴 하네

col, row 이중 반복문을 일단 len(a[0])의 range로 돌면서 operator의 getitem 이용

왼쪽 회전은 reversed 이용

함수 시그니처는 pixel_matrix: list[list[int]] <- 마지막 int는 4바이트를 표현하는 임의의
타입이어도 상관 없음

-> pixel_matrix, rotation_direction -> list[list[int]]일 듯

행렬을 추가적으로 사용하는 부분이 transpose 부분인데, 이걸 iterator 버전으로 작성하면,
명시적 행렬 추가 없이 작성 가능

```

```py
from typing import Literal
Image = list[list[int]]
Rotation = Literal("left", "right")

def roatate_image(pixel_matrix: Image, rotation_type: Rotation) -> Image:
    switch rotation_type:
        case "left":
            # each element order in a row reversed, each row order in the matrix preserved
            transpose_target = []
            for row in pixel_matrix:
                t_row = reversed(row)
                transpose_target.append(t_row)
            return transpose(transpose_target)
            # return list(gen_transpose(transpose_target))
        case "right":
            # each element order in a row preserved, each row order in the matrix reversed
            transpose_target = []
            for row in reversed(pixel_matrix):
                t_row = row
                transpose_target.append(t_row)
            return transpose(transpose_target)

def transpose(image: Image) -> Image:
    from operation import getitem
    num_of_row = len(image)
    row_size = len(image[0])
    transpose_target = []
    for i in range(row_size):
        t_row = [getitem(row, i) for row in image]
        transpose_target.append(t_row)
    return t_row

def gen_transpose(image: Image):
    from operation import getitem
    num_of_row = len(image)
    row_size = len(image[0])
    transpose_target = []
    for i in range(row_size):
        yield list(getitem(row, i) for row in image)
```

01_01_08 0 행렬: M * N 행렬의 한 원소가 0일 경우, 해당 원소가 속한 행과 열의 모든 원소를
0으로 설정하는 알고리즘을 작성하라.

```whiteboard
step1: [False] * M 인 zero_row_info, [False] * N 인 zero_col_info를 선언
step2: 행렬을 행별, 열별로 읽으며 0가 나올 때 마다 해당 열과 행의 zero_row/col_info를
True로 변환
step3: 행렬을 다시 읽으며 zero_row/col_info가 True가 아닌 경우에만 원래의 원소로 치환,
그렇지 않은 경우 0으로 fill

-> 공간복잡도 O(M * N)으로 최소
```

```py
def zero_fill(A: list[list[int]]) -> list[list[int]]:
    m = len(A)
    n = len(A[0])

    zero_row_info = [False] * m
    zero_col_info = [False] * n

    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                zero_row_info[i] = True
                zero_col_info[j] = True

    for i in range(m):
        for j in range(n):
            if zero_row_info[i] or zero_col_info[j]:
                A[i][j] = 0

    return A
```

01_01_09 문자열 회전: 한 단어가 다른 문자열에 포함되어 있는지 판별하는 isSubstring이라는
메서드가 있다고 하자. s1과 s2의 두 문자열이 주어졌고, s2가 s1을 회전시킨 결과인지
판별하고자 한다(가령 'waterbottle'은 'erbottlewat'을 회전시켜 얻을 수 있는 문자열이다).
isSubstring 메서드를 한번만 호출해서 판별할 수 있는 코드를 작성하라

```whiteboard
s2가 s1을 회전시킨 결과라면, s2는 두 부분으로 나뉘어진다.
어떤 인덱스 i가 존재하여
s2[:i]와 s2[i:]를 이용하여 s1을 재구성할 수 있다.
정확히는 s2[i:] + s2[:i] == s1이다. i >= 0, i < n

이런 경우, s2 + s2 안에 s1은 반드시 한번(혹은 두번) 존재하게 된다.
s2 + s2를 생각하자.
s1이 isSubstring인지 보면 끝나네

s1:aabacaaabb
s2:caaabbaaba

```

```py
def is_rotation_equivalent(txt1: str, txt2: str) -> bool:
    target_sentence = txt2 + txt2
    return isSubstring(txt1, txt2)

# where isSubstring(word: str, sentence: str) -> bool
# holds if word is substring of sentence
```
