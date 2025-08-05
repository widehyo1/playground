import sys
input = sys.stdin.readline

class StackNode:
    def __init__(self, data, next_=None):
        self.data = data
        self.next_ = next_

    def __repr__(self):
        return f"<StackNode ({self.data}) >"

class Stack:
    def __init__(self, head):
        self.head = head

def longest_increasing_subsequence_size(numbers: list[int]) -> int:
    n = len(numbers)
    size = 0

    stack = Stack(StackNode((0, None, 0)))

    while stack.head:
        print(stack.head)
        cur = stack.head.data
        idx, seen_max, cur_size = cur
        stack.head = stack.head.next_

        if cur_size + (n - idx) <= size:
            continue

        if idx == n:
            size = max(size, cur_size)
            continue

        number = numbers[idx]
        new_stack_node = StackNode((idx + 1, seen_max, cur_size))
        new_stack_node.next_ = stack.head
        stack.head = new_stack_node
        if seen_max is None:
            new_stack_node = StackNode((idx + 1, number, 1))
            new_stack_node.next_ = stack.head
            stack.head = new_stack_node
        elif seen_max < number:
            new_stack_node = StackNode((idx + 1, number, cur_size + 1))
            new_stack_node.next_ = stack.head
            stack.head = new_stack_node

    return size

n = int(input())
numbers = [int(number) for number in input().split()]
res = longest_increasing_subsequence_size(numbers)
print(res)
