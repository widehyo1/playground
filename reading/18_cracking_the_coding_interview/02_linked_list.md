02_01. 중복 없애기: 정렬되어 있지 않은 연결리스트가 주어졌을 때 이 리스트에서 중복되는
원소를 제거하는 코드를 작성하라.
연관문제 - 임시 버퍼를 사용할 수 없다면 어떻게 풀 수 있을까?

```whiteboard
단방향 연결리스트라고 가정하고 풀겠습니다. ListNode가 val과 nxt를 가지는 구조,
LinkedList는 head로 ListNode를 가지는 class.

임시 버퍼 set을 하나 선언하고
한번은 순회해야 하니까 한 원소씩 읽으면서 set에 없다면 추가하고 그대로 pointer를
이동시키고 있다면 next의 next로 수정하겠습니다.

두번 이상 반복되는 경우가 문제될 수 있는데
그림을 그려보죠
2 > 3 > 1 > 2 > 2 > 6
vvvvvv
231226
1, 2
2, 2 3
3, 2 3 1
4, 2 3 1
5, 2 3 1
6, 2 3 1 6

base case 처리는 0일때 0
1일때 그대로 return

value가 hashable한지 물어봐야겠음
event가 발생되는 경우만 직전 포인터를 갱신하게 되네

two pointer cur_node와 prev_node
(3, 2) event 발생 2의 next를 cur_node로 설정
prev_node갱신 
(1, 3) ""
(2, 1) event 미발생, prev는 여전히 1
cur만 다음으로
(2, 1) ""
(6, 1) event 발생, prev의 next를 cur로 설정

루프 종료

prev의 next를 None으로 설정

head 반환

임시버퍼가 무슨 의미인지 물어보기
만약 임시버퍼 사용 불가하면 bit masking 이용 <- 새로운 것인지는 어떻게 알지?
해당하는 값의 명확한 인덱스가 있어야만 가능할듯

Q 양방향 연결리스트인 경우의 풀이는?

```

```py
class LinkNode:
    def __init__(self, val: int, nxt: "LinkNode" = None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    def __init__(self, head: LinkNode = None):
        self.head = head

def remove_duplicate(llist: LinkedList) -> LinkedList:
    head = llist.head
    if head is None:
        return llist
    cur_node = head.nxt
    if cur_node is None:
        return llist
    distinct_value_set = set()
    distinct_value_set.add(head.val)
    prev_node = head
    while cur_node:
        if cur_node.val in distinct_value_set:
            cur_node = cur_node.nxt
        else:
            distinct_value_set.add(cur_node.val)
            cur_node, prev_node = cur_node.nxt, cur_node
            prev_node.nxt = cur_node
    prev_node.nxt = None
    return LinkedList(head)
```

02_02 뒤에서 k번째 원소 구하기: 단방향 연결리스트가 주어졌을 때 뒤에서 k번째 원소를 찾는
알고리즘을 구현하라.

```whiteboard
주어진 연결리스트의 head부터 시작하여 k번 next로 이동합니다.
이동이 불가한 경우 length가 k미만이므로 None이나 error 처리 방법을 정하면 됩니다.
여기선 None 리턴으로 처리하겠습니다.

fst_pointer와 snd_pointer를 이용해서 한번 이동할 때 두 pointer를 한칸씩 이동하고 next가
None인 경우 snd_pointer의 value를 구하면 됩니다.

```

02_03 중간 노드 삭제: 단방향 연결리스트가 주어졌을 때 중간(정확히 가운데 노드일 필요는
없고 처음과 끝 노드만 아니면 된다)에 있는 노드 하나를 삭제하는 알고리즘을 구현하라. 단,
삭제할 노드에만 접근할 수 있다.

```whiteboard
일단, 삭제할 노드에만 접근할 수 있다는 것이 무슨 의미인지 좀 더 자세히 질문
만약 삭제할 노드에 해당하는 ListNode만 접근가능 하다면 이전 노드의 next를 변경해야 하는 이
상황에서 이전 노드를 접근할 수 없으므로 문제를 풀 수 없다.

세상에... 틀렸네. 천재신데요?
```

```py
def skip_node(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next
```

02_04 분할: 값 x가 주어졌을 때 x보다 작은 노드들을 x보다 크거나 같은 노드들보다 앞에
오도록 하는 코드를 작성하라. 만약 x가 리스트에 있다면 x는 그보다 작은 원소들보다 뒤에
나오기만 하면 된다. 즉 원소 x는 '오른쪽 그룹'어딘가에만 존재하면 된다. 왼쪽과 오른쪽 그룹
사이에 있을 필요는 없다.

```whiteboard
노드를 재배치하는 문제, fst와 snd를 이용해서 나누자
fst가 없는 경우는 그대로 반환
snd가 없는 경우도 그대로 반환
fst와 snd가 모두 있는 경우는 fst의 마지막을 snd의 처음과 연결시키면 됨
값은 real number로 가정
```


```py
def partition(llist: LinkedList, x):
    fst = None
    fst_head = None
    snd = None
    snd_head = None

    head = llist.head
    if head is None:
        return llist

    cur = head

    # move current node to last element
    while cur.next is not None:
        cur_val = cur.val
        if cur.val > x:
            snd, snd_head = add_group(cur, snd, snd_head)
        else:
            fst, fst_head = add_group(cur, fst, fst_head)
        cur = cur.next
    if cur.val > x:
        snd, snd_head = add_group(cur, snd, snd_head)
    else:
        fst, fst_head = add_group(cur, fst, fst_head)

    if snd_head is None:
        return llist

    if fst_head is None:
        return llist

    snd.next = None
    fst.next = snd_head
    return LinkedList(fst_head)
```

02_05 리스트의 합: 연결리스트로 숫자를 표현할 때 각 노드가 자시수 하나를 가리키는 방식으로
표현할 수 있다. 각 숫자는 역순으로 배열되어 있는데, 첫 번째 자리수가 리스트의 맨 앞에
위치하도록 배열된다는 뜻이다. 이와 같은 방식으로 표현된 숫자 두개가 있을 때, 이 두 수를
더하여 그 합을 연결리스트로 반환하는 함수를 작성하라

입력: (7->1->6)+(5->9->2). 즉, 617+295
출력: 2->1->9. 즉, 912

연관문제
각 자릿수가 정상적으로 배열된다고 가정하고 같은 문제를 풀어보자.

```whiteboard
일의 자리수끼리 더하고 10보다 커지는지 아닌지에 따라
결과 리스트에 두 개를 

vvv
716
592

- 0
5
7
12 2->1

- 1
1
9
1
11 1->1

- 2
6
2
1
9

219

99999
1

10: 0->1
(9, 1), carry: True
(9), carry: True
(9), carry: True
(9), carry: True
(9), carry: True
(), carry: False

값을 추적할 때는 carry 플래그만 있으면 됨
순서 필요 없네. 없으면 넣지 않으면 됨

세 개의 리스트... 세개가 필요할까?
일단 자리수 + 어디에서 왔는지 파악하는건 필요

walker는 index 따라서 증가
None을 

carry가 True거나 아직 남은 자리수가 있다면

일단, 음수는 아닌지 먼저 물어봐야되네

근데 이거 사실 가장 쉽게 푸는건 그냥 숫자로 바꿔버리는거네
숫자 to linkedlist만 있으면 되는구나

연관문제는 내 방식으로 한다면 각 linked list를 reverse한다음 똑같이 푼다음 다시
reverse하면 됨

> 그럼 reverse를 어떻게 만들지?
재귀 돌릴까?
재귀보다 포인터가 더 strait forword한듯?
5개
head와 1, 4
12345
2345 -> 5432
(1,2)(2,3)(3,4)(4,5)
1은 next를 None으로 설정
각각 두번째 것의 next를 앞노드로 설정
더이상 없으니 해당노드를 head로 설정
```


```py
def add_two_number(llist1, llist2):
    carry = 0
    fst_node, snd_node = llist1.head, llist2.head

    head = ListNode(None)
    curnode = head

    while fst_node or snd_node or carry == 1:
        step_val = 1 if carry else 0
        if fst_node is not None:
            step_val += fst_node.val
            fst_node = fst_node.next
        if snd_node is not None:
            step_val += snd_node.val
            snd_node = snd_node.next
        carry, step_val = divmod(step_val, 10)
        newnode = ListNode(step_val)
        curnode.next = newnode
        curnode = newnode

    return head


def add_two_number(llist1, llist2):
    carry = 0
    fst_node, snd_node = llist1.head, llist2.head

    head = ListNode(None)
    curnode = head

    while fst_node or snd_node or carry == 1:
        step_val = 1 if carry else 0
        if fst_node is not None:
            step_val += fst_node.val
            fst_node = fst_node.next
        if snd_node is not None:
            step_val += snd_node.val
            snd_node = snd_node.next
        carry, step_val = divmod(step_val, 10)
        newnode = ListNode(step_val)
        curnode.next = newnode
        curnode = newnode

    return LinkedList(head.next)
```

02_06 회문: 주어진 연결리스트가 회문(palindrome)인지 검사하는 함수를 작성하라.
```whiteboard
일단 양방향


1234
1,2->2,4


12345
1,2->2,4

짝수 홀수는 가능하네
홀수인 경우 중간 바로 잡을 수 있고
짝수인 경우는 뭐 가능하네

양방향 리스트인 경우 홀수인 경우 중간에서 시작해서 양방향으로 가면서 다른게 나오면 break
끝까지 가면 True리턴
짝수인 경우에는 중간의 두개를 left, right라고 하고 양방향으로 가면서 다른게 나오면 break

단방향 리스트인 경우?
중간 버퍼 하나 두는게 가장 깔끔하겠는데?
중간을 찾을 때까지 하나씩 append한다음
역방향으로 읽으며 같은지 확인
```

```py
class LinkNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class DoubleLinkNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def is_palindrome(node: LinkNode) -> bool:
    if node.nxt is None:
        return True
    head = node
    if head.nxt.nxt is None:
        return head.val == head.nxt.val
    fst = head
    snd = head
    comp = []
    while snd.nxt.nxt:
        comp.append(fst.val)
        snd = snd.nxt.nxt
        fst = fst.nxt
    if snd.nxt is None:
        # list is even
        #  v
        # 1234
        #    ^
        idx = -1
        while fst.nxt:
            fst = fst.nxt
            if fst.val != comp[idx]:
                return False
            idx -= 1
        return True
    else:
        # list is odd
        #  v
        # 12345
        #    ^
        fst = fst.nxt.nxt
        idx = -1
        while fst.nxt:
            if fst.val != comp[idx]:
                retrun False
            fst = fst.nxt
            idx -= 1
        return True


def is_palindrome(dnode: DoubleLinkNode) -> bool:
    if node.nxt is None:
        return True
    head = node
    if head.nxt.nxt is None:
        return head.val == head.nxt.val
    fst = head
    snd = head
    while snd.nxt.nxt:
        comp.append(fst.val)
        snd = snd.nxt.nxt
        fst = fst.nxt
    if snd.nxt is None:
        # list is even
        #  v
        # 1234
        #    ^
        left = fst
        right = fst.nxt
        while left.prev and right.nxt:
            if left.val != right.val:
                return False
            left = left.prev
            right = right.nxt
        return True
    else:
        # list is odd
        #  v
        # 12345
        #    ^
        left = fst.nxt
        right = fst.nxt
        while left.prev and right.nxt:
            if left.val != right.val:
                return False
            left = left.prev
            right = rigth.nxt
        return True
```

02_07 교집합: 단방향 연결리스트 두 개가 주어졌을 때 이 두 리스트의 교집합 노드를 찾은 뒤
반환하는 코드를 작성하라. 여기서 교집합이란 노드의 값이 아니라 노드의 주소가 완전히 같은
경우를 말한다. 즉, 첫번째 리스트에 있는 k번째 노드와 두 번째 리스트에 있는 j번째 노드가
주소까지 완전히 같다면 이 노드는 교집합의 원소가 된다.

```whiteboard
일단 하나라도 교집합을 찾으면 그 뒤는 모두 교집합 노드가 된다.
가장 먼저 생각할 수 있는건 O(nm)이 걸리는 풀이
첫번째 노드와 두번째 연결리스트의 모든 노드와 비교하여 같으면 모든 노드 반환
같지 않다면 첫번째 노드의 next에 대하여 같은 작업 반복

근데 그럴필요가 있나?
주소를 set에 넣으면 되잖아

근데, 단방향 연결리스트가 사이클이 있는지는 따져봐야하네

두번째 노드를 순회하면서 주소값을 모아 set을 만들자
만약 같은 노드를 발견하면 해당 노드를 마킹하고 멈춤

첫 번째 노드의 주소를 이 셋과 비교하면서 있는지 판단
없다면 다음으로 가고 있으면 해당 노드부터 끝까지 리턴(사이클 없을 때)
사이클이 있다면 현재 주소부터 새로운 set을 만들어서 같은 노드 나올 때까지 반환에 추가
같은 노드 나오면 break
```

```py
class LinkNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

def intersection(node1: ListNode, node2: ListNode) -> list[ListNode]:
    snd_set = set()
    while node2.nxt:
        curid = id(node2)
        if curid in snd_set:
            break
        snd_set.add(curid)
        node2 = node2.nxt
    snd_set.add(id(node2))
    result = []
    fst_set = set()
    flag = False
    while node1.nxt:
        curid = id(node1)
        flag = curid in snd_set
        if curid in fst_set:
            break
        fst_set.add(curid)
        if flag:
            result.append(node1)
        node1 = node1.nxt
    if id(node1) in snd_set:
        result.append(node1)
    return result
```

02_08 루프 발견: 수노한 연결리스트(circular lilnked list)가 주어졌을 때, 순환되는 부분의
첫째 노드를  반환하는 알고리즘을 작성하라. 순환 연결리스트란 노드의 next 포인터가 앞선
노드들 가운데 어느 하나를 가리키도록 설정되어있는, 엄밀히 말해서 변질된 방식의
연결리스트를 의미한다.


```whiteboard
```
```py
class LinkNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

def circular_head(node: ListNode) -> ListNode:
    id_set = set()
    while node.nxt:
        curid = id(node)
        if curid in id_set:
            return node
        id_set.add(curid)
        node = node.nxt
```
