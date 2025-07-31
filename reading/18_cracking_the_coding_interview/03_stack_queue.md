03_01 한개로 세 개: 배열 한 개로 스택 세 개를 어떻게 구현할지 설명하라.

```whiteboard
문제 설명이 더 필요합니다...
```

03_02 스택 Min: 기본적인 push와 pop 기능이 구현된 스택에서 최솟값을 반환하는 min 함수를
추가하려고 한다. 어떻게 설계할 수 있겠는가? push, pop, min 연산은 모두 O(1) 시간에
동작해야 한다.

```whiteboard
push, pop하는 동시에 min이 없데이트 되게 하면 된다.
이거 counter를 가지고 있어야 하나?
heappop, heappush은 O(1)이 안되는데



class StackNode:
    def __init__(self, data, next_):
        self.data = data
        self.next_ = next_

class Stack:
    def __init__(self, top: StackNode=None, min_=None, min_count=0):
        self.top = top
        self.min_ = min_
        self.min_count = 0

    def push(self, val):
        stack_node = StackNode(val)
        if self.top:
            stack_node._next = self.top
            self.top = stack_node
            if self.min_ > val:
                self.min_ = val
                self.min_count = 1
            elif self.min_ == val:
                self.min_count += 1
        else:
            self.top = stack_node
            self.min_ = val

    def pop(self):
        if self.top is None:
            raise RuntimeException("EmptyStack error")
        
        self.top = self.top.next_
```
